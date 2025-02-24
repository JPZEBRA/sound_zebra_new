import numpy as np
import math

from aoki.biquad_filter import LPF
from aoki.biquad_filter import BPF
from aoki.biquad_filter import filter

def sin_out(sound_a,duration,note,pow,sampling):

    freq = sound_a * np.power(2, note / 12)

    return sin_freq_out(sound_a,duration,freq,pow,sampling)

def sin_freq_out(sound_a,duration,freq,pow,sampling):

    length_of_s = int(duration)
    so = np.zeros(length_of_s)

    f0 = freq
    T = 1 / f0

    for n in range(length_of_s):

        so[n] = pow * np.sin(2 * np.pi * f0/sampling*n)

    return so

def tri_out(sound_a,duration,note,pow,sampling):

    freq = sound_a * np.power(2, note / 12)

    return tri_freq_out(sound_a,duration,freq,pow,sampling)

def tri_freq_out(sound_a,duration,freq,pow,sampling):

    length_of_s = int(duration)
    so = np.zeros(length_of_s)

    f0 = freq
    T = 1 / f0

    for n in range(length_of_s):
        pos = f0/sampling*n
        pos -= math.floor(pos)
        if pos < 0.5 : so[n] = pow * pos * 2 - 0.5 * pow
        else :         so[n] = pow * ( 1.0 - (pos - 0.5) * 2) - 0.5 * pow

    return so

def square_out(sound_a,duration,note,pow,sampling):

    return pulse_out(sound_a,duration,note,0.5,pow,sampling)

def square_freq_out(sound_a,duration,freq,pow,sampling):

    return pulse_freq_out(sound_a,duration,freq,0.5,pow,sampling)

def pulse_out(sound_a,duration,note,ratio,pow,sampling):

    freq = sound_a * np.power(2, note / 12)

    return pulse_freq_out(sound_a,duration,freq,ratio,pow,sampling)

def pulse_freq_out(sound_a,duration,freq,ratio,pow,sampling):

    f0 = freq
    T = 1 / f0

    length_of_s = int(duration)
    so = np.zeros(length_of_s)

    for n in range(length_of_s):
        pos = f0/sampling*n
        pos -= math.floor(pos)
        if pos < ratio : so[n] = pow

    return so

def pulse_out_mod(sound_a,duration,note,mod,pow,sampling):

    freq = sound_a * np.power(2, note / 12)

    return pulse_out_freq_mod(sound_a,duration,freq,mod,pow,sampling)

def pulse_out_freq_mod(sound_a,duration,freq,mod,pow,sampling):

    length_of_s = int(duration)
    so = np.zeros(length_of_s)

    f0 = freq
    T = 1 / f0

    for n in range(length_of_s):
        pos = f0/sampling*n
        pos -= math.floor(pos)
        if pos < 0.5 + mod[n] : so[n] = pow

    return so

def sawtooth_out(sound_a,duration,note,pow,sampling):

    freq = sound_a * np.power(2, note / 12)

    return sawtooth_freq_out(sound_a,duration,freq,pow,sampling)

def sawtooth_freq_out(sound_a,duration,freq,pow,sampling):

    length_of_s = int(duration)
    so= np.zeros(length_of_s)

    f0 = freq
    T = 1 / f0

    for n in range(length_of_s):
        saw = (f0/sampling*n)
        saw -= int(saw)
        so[n] = saw - 0.5

    return so

def sin_decay(sound_a,duration,note,pow,sampling,decay):

    freq = sound_a * np.power(2, note / 12)
    T = 1 / f0

    return sin_freq_decay(sound_a,duration,freq,pow,sampling,decay)

def sin_freq_decay(sound_a,duration,freq,pow,sampling,decay):

    length_of_s = int(duration)
    so = np.zeros(length_of_s)

    f0 = freq
    T = 1 / f0

    for n in range(length_of_s):

        dec = np.power(np.e , - n * decay / duration )

        so[n] = pow * dec * np.sin(2 * np.pi * f0/sampling*n)

    return s

def square_decay(sound_a,duration,note,pow,sampling,decay):

    length_of_s = int(duration)
    s = np.zeros(length_of_s)

    f0 = sound_a * np.power(2, note / 12)
    T = 1 / f0

    for n in range(length_of_s):

        sw = np.sin(2 * np.pi * f0/sampling*n)
        if sw > 0 : s[n] =   pow
        if sw < 0 : s[n] = - pow

        dec = np.power(np.e , - n * decay / duration )
        s[n] *= dec

    return s

def pulse_decay(sound_a,duration,note,ratio,decay,pow,sampling):

    length_of_s = int(duration)
    s = np.zeros(length_of_s)

    f0 = sound_a * np.power(2, note / 12)
    T = 1 / f0

    for n in range(length_of_s):

        pos = f0/sampling*n
        pos -= math.floor(pos)
        if pos < ratio : s[n] = pow

        dec = np.power(np.e , - n * decay / duration )
        s[n] *= dec

    return s

def sawtooth_decay(sound_a,duration,note,pow,sampling,decay):

    length_of_s = int(duration)
    s = np.zeros(length_of_s)

    f0 = sound_a * np.power(2, note / 12)

    T = 1 / f0


    for n in range(length_of_s):

        saw = (f0/sampling*n)
        saw -= int(saw)
        s[n] = saw - 0.5

        dec = np.power(np.e , - n * decay / duration )
        s[n] *= dec

    return s

def sin_jitter(freq,jitter,duration,sampling):

    length_of_s = int(duration)

    s = np.zeros(length_of_s)

    j = 0

    for n in range(length_of_s) :

        j += jitter[n]

        s[n] = np.sin( 2 * np.pi * ( freq / sampling * n + j / sampling ) )

    return s


def white_noise(duration) :

    s = np.zeros(duration)

    mean = 0

    for n in range(duration) :

        s[n] = ( np.random.rand()*2 ) - 1

        mean += s[n]

    mean /= duration

    for n in range(duration) :

        s[n] -= mean

    return s

def color_noise(sound_a,duration,note,sampling) :

    f0 = sound_a * np.power(2,note/12)

    T = 1/f0

    length_s = duration

    s0 = np.zeros(length_s)

    np.random.seed(0)

    for n in range(length_s) :

        s0[n] = ( np.random.rand()*2 ) - 1

    if(f0 < 20000) :

        Q = 1 / np.sqrt(2)

        a,b = LPF(sampling,f0*10,Q)

        s1 = filter(a,b,s0)

        s0 = s1

    return s0

def sound_noisy(sound_a,duration,note,rate,sampling) :

    f0 = sound_a * np.power(2,note/12)

    f1 = f0 * rate

    T = 1/f0

    s0 = color_noise(sound_a,duration,note,sampling)

    if(f1 < 20000) :

        Q = 200

        a,b = BPF(sampling,f1,Q)

        s1 = filter(a,b,s0)

        s0 = s1

    return s0

def sound_string(sound_a,duration,note,sampling) :

    f_c = 0.985
    f_d = 0.7

    f0 = sound_a * np.power(2,note/12)

    T = 1/f0

    D = int(T*sampling)
  
    s0 = white_noise(D+1)

    length_of_s = int(duration)

    s = np.zeros(length_of_s)

    for n in range(D+1):
        s[n] = s0[n]

    for n in range(D+1,length_of_s):
        s[n] = f_c*(f_d*s[n-D] + (1-f_d)*s[n-D-1])

    return s

def FM_out(sound_a,duration,note,pw,ratio,pw_m,sampling):

    length_of_s = int(duration)
    s = np.zeros(length_of_s)

    f0 = sound_a * np.power(2, note / 12)
    fm = f0*ratio

    for n in range(length_of_s):
        md = np.sin(2 * np.pi * fm / sampling * n)
        cr = np.sin(2 * np.pi * f0 / sampling * n)
        s[n] = pw * ( cr + pw_m * md )

    return s
