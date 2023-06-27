import numpy as np

ADSR_A = 0.01
ADSR_D = 0.10
ADSR_S = 1.00
ADSR_R = 0.30
ADSR_DEPT = 1.05

def set_ADSR_HARD() :

    global ADSR_A
    global ADSR_D
    global ADSR_S
    global ADSR_R
    global ADSR_DEPT

    ADSR_A = 0.00
    ADSR_D = 0.00
    ADSR_S = 1.00
    ADSR_R = 0.00
    ADSR_DEPT = 1.00

def set_ADSR_GENTRE() :

    global ADSR_A
    global ADSR_D
    global ADSR_S
    global ADSR_R
    global ADSR_DEPT

    ADSR_A = 0.30
    ADSR_D = 0.30
    ADSR_S = 1.00
    ADSR_R = 0.10
    ADSR_DEPT = 1.01

def set_ADSR_SOFT() :

    global ADSR_A
    global ADSR_D
    global ADSR_S
    global ADSR_R
    global ADSR_DEPT

    ADSR_A = 0.08
    ADSR_D = 0.03
    ADSR_S = 1.00
    ADSR_R = 0.30
    ADSR_DEPT = 1.05

def set_ADSR_IDIOT() :

    global ADSR_A
    global ADSR_D
    global ADSR_S
    global ADSR_R
    global ADSR_DEPT

    ADSR_A = 0.01
    ADSR_D = 0.30
    ADSR_S = 0.95
    ADSR_R = 0.20
    ADSR_DEPT = 1.50


def sin_out_ADSR(sound_a,duration,note,pow,sampling):

    length_of_s = int(duration)
    s = np.zeros(length_of_s)

    f0 = sound_a * np.power(2, note / 12)
    T = 1 / f0

    delta = 0

    for n in range(length_of_s):

        s[n] = pow * np.sin(2 * np.pi * delta)

        ft = freq_ADSR(f0,n,duration)

        delta = delta + ft/sampling

    return s

def freq_ADSR(fbase,pos,duration) :

    np = pos/duration

    if np < ADSR_A : return fbase * ADSR_DEPT * np / ADSR_A

    if np < ADSR_A + ADSR_D : return fbase * ADSR_DEPT - ( fbase * ADSR_DEPT - fbase * ADSR_S ) * ( np - ADSR_A ) / ADSR_D

    if np < 1.0 - ADSR_R : return fbase

    return fbase * (1.0 - np ) / ADSR_R

