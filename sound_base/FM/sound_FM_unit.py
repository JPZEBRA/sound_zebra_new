import numpy as np
import math

from sound_base.color.sound_color import white_noise
from sound_base.effect.sound_effector import BPFilter

from sound_base.FM.sound_FM_envelope import set_FME
from sound_base.FM.sound_FM_envelope import set_FME

# GET-FREQ

def Freq(sound_a,note) :

    freq = sound_a * np.power(2, note / 12)

    return freq

# SIN-NOTE

def SINNote(sound_a,duration,note,ratio,feedback,sampling):

    freq = Freq(sound_a, note)
 
    return SINFreq(sound_a,duration,freq,ratio,feedback,sampling)

# SIN-FREQ

def SINFreq(sound_a,duration,freq,ratio,feedback,sampling):

    length_of_s = int(duration)
    so = np.zeros(length_of_s)

    f0 = freq
    fm = f0*ratio

    sb = 0

    for n in range(length_of_s):
        pos = fm / sampling * n + sb * feedback
        so[n] = np.sin(2 * np.pi * pos)
        sb = so[n]

    return so

# COS-NOTE

def COSNote(sound_a,duration,note,ratio,feedback,sampling):

    freq = Freq(sound_a, note)

    return COSFreq(sound_a,duration,freq,ratio,feedback,sampling)

# COS-FREQ

def COSFreq(sound_a,duration,freq,ratio,feedback,sampling):

    length_of_s = int(duration)
    so = np.zeros(length_of_s)

    f0 = freq
    fm = f0*ratio

    sb = 0

    for n in range(length_of_s):
        pos = fm / sampling * n + sb * feedback
        so[n] = np.cos(2 * np.pi * pos)
        sb = so[n]

    return so

# COLOR NOISE

def CNoiseNote(sound_a,duration,note,ratio,sampling):

    freq = Freq(sound_a, note)

    return CNoiseFreq(sound_a,duration,freq,ratio,sampling)

def CNoiseFreq(sound_a,duration,freq,ratio,sampling):

    sa = white_noise(duration)

    so = BPFilter(sampling,sa,freq,0.3,0.0)

    return so

############
# FM-SOUND #
############

# FM-EMV

def SETEnv(sound,speed):

    so = set_FME(sound,speed)

    return so

# MIX

def Mix(s1,s2,ratio):

    length_of_s = len(s1)
    so = np.zeros(length_of_s)

    for n in range(length_of_s):
         so[n] = s1[n]*ratio + s2[n]*(1.0 - ratio)

    return so

# MODULATE

def Modulate(s1,s2,power,feedback):

    length_of_s = len(s1)
    so = np.zeros(length_of_s)

    sb = 0

    p = 0

    for n in range(length_of_s):

        diff = power * (s2[n] + sb * feedback)
        if n > 0 : diff += 1.0

        i = math.floor(p)
        r = p - i
 
        if i < 0 :
            so[n] = s1[i]
        elif i < length_of_s - 1 :
            so[n] = s1[i]*(1-r) + s1[i+1]*r
        elif i < length_of_s :
            so[n] = s1[i]
        else :
            so[n] = s1[n]

        sb = so[n]

        p += diff

    return so

# SYNC

def Sync(s1,s2):

    length_of_s = len(s1)
    so = np.zeros(length_of_s)

    sp = 0

    for n in range(length_of_s):

        if n > 0 and n < length_of_s - 1 and s2[n] < s2[n-1] and s2[n] <= s2[n+1] : sp = 0

        so[n] = s1[sp]

        sp += 1
 
    return so
