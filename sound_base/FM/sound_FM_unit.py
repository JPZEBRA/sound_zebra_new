import numpy as np
import math

from sound_base.FM.sound_FM_envelope import set_FME

# GET-FREQ
def Freq(sound_a,note) :

    freq = sound_a * np.power(2, note / 12)

    return freq

# SIN-NOTE
def SINNote(sound_a,duration,note,ratio,feedback,sampling):

    length_of_s = int(duration)
    s = np.zeros(length_of_s)

    f0 = Freq(sound_a, note)
    fm = f0*ratio

    sb = 0

    for n in range(length_of_s):
        pos = fm / sampling * n + sb * feedback
        s[n] = np.sin(2 * np.pi * pos)
        sb = s[n]

    return s

# SIN-FREQ
def SINFreq(sound_a,duration,freq,ratio,feedback,sampling):

    length_of_s = int(duration)
    s = np.zeros(length_of_s)

    f0 = freq
    fm = f0*ratio

    sb = 0

    for n in range(length_of_s):
        pos = fm / sampling * n + sb * feedback
        s[n] = np.sin(2 * np.pi * pos)
        sb = s[n]

    return s

# FM-SOUND

# FM-EMV
def SETEnv(sound,duration):

    so = set_FME(sound,duration)

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

    for n in range(length_of_s):

        diff =  power * (s2[n] + sb * feedback)
        p = math.floor(n + diff)
        r = n + diff - p
 
        if p < 0 :
            so[n] = s1[n]
        elif p < length_of_s - 1 :
            p = math.floor(n + diff)
            r = n + diff - p
            so[n] = s1[p]*(1-r) + s1[p+1]*r
        elif p < length_of_s :
            so[n] = s1[p]
        else :
            so[n] = s1[n]

        sb = so[n]
 
    return so

# MODULATE-R
def ModulateR(s1,s2,power,feedback,freq,sampling):

    length_of_s = len(s1)
    so = np.zeros(length_of_s)

    pr = sampling / freq
   

    sb = 0

    for n in range(length_of_s):

        mp = int(n - math.floor(n/pr) * pr)

        diff =  power * (s2[mp] + sb * feedback)
        p = math.floor(n + diff)
        r = n + diff - p
 
        if p < 0 :
            so[n] = s1[n]
        elif p < length_of_s - 1 :
            p = math.floor(n + diff)
            r = n + diff - p
            so[n] = s1[p]*(1-r) + s1[p+1]*r
        elif p < length_of_s :
            so[n] = s1[p]
        else :
            so[n] = s1[n]

        sb = so[n]
 
    return so

