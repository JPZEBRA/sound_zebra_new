import numpy as np

def sin_out(sound_a,duration,note,pow,sampling):

    length_of_s = int(duration)
    s = np.zeros(length_of_s)

    f0 = sound_a * np.power(2, note / 12)
    T = 1 / f0


    for n in range(length_of_s):
        s[n] = pow * np.sin(2 * np.pi * f0/sampling*n)

    return s

def square_out(sound_a,duration,note,pow,sampling):

    length_of_s = int(duration)
    s = np.zeros(length_of_s)

    f0 = sound_a * np.power(2, note / 12)
    T = 1 / f0


    for n in range(length_of_s):
        sw = np.sin(2 * np.pi * f0/sampling*n)
        if sw > 0 : s[n] =   pow
        if sw < 0 : s[n] = - pow

    return s

def pulse_out(sound_a,duration,note,pow,sampling):

    length_of_s = int(duration)
    s = np.zeros(length_of_s)

    f0 = sound_a * np.power(2, note / 12)
    T = 1 / f0


    for n in range(length_of_s):
        sw = np.sin(2 * np.pi * f0/sampling*n)
        if sw >  0.99 : s[n] =   pow
        if sw < -0.99 : s[n] = - pow

    return s

def sawtooth_out(sound_a,duration,note,pow,sampling):

    length_of_s = int(duration)
    s = np.zeros(length_of_s)

    f0 = sound_a * np.power(2, note / 12)
    T = 1 / f0


    for n in range(length_of_s):
        saw = (f0/sampling*n)
        saw -= int(saw)
        s[n] = saw - 0.5

    return s

def sin_decay(sound_a,duration,note,pow,sampling,decay):

    length_of_s = int(duration)
    s = np.zeros(length_of_s)

    f0 = sound_a * np.power(2, note / 12)
    T = 1 / f0

    for n in range(length_of_s):

        dec = np.power(np.e , - n * decay / duration )

        s[n] = pow * dec * np.sin(2 * np.pi * f0/sampling*n)

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

