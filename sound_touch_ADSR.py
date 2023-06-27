import numpy as np

TADSR_A = 0.01
TADSR_D = 0.10
TADSR_S = 1.00
TADSR_R = 0.30
TADSR_DEPT = 1.05

def set_touch_HARD() :

    global TADSR_A
    global TADSR_D
    global TADSR_S
    global TADSR_R
    global TADSR_DEPT

    TADSR_A = 0.01
    TADSR_D = 0.20
    TADSR_S = 0.30
    TADSR_R = 0.50
    TADSR_DEPT = 2.00

def set_touch_GENTRE() :

    global TADSR_A
    global TADSR_D
    global TADSR_S
    global TADSR_R
    global TADSR_DEPT

    TADSR_A = 0.30
    TADSR_D = 0.30
    TADSR_S = 1.00
    TADSR_R = 0.10
    TADSR_DEPT = 1.01

def set_touch_SOFT() :

    global TADSR_A
    global TADSR_D
    global TADSR_S
    global TADSR_R
    global TADSR_DEPT

    TADSR_A = 0.08
    TADSR_D = 0.03
    TADSR_S = 1.00
    TADSR_R = 0.30
    TADSR_DEPT = 1.05

def touch_ADSR(sound):

    duration = len(sound)

    s = np.zeros(duration)

    for n in range(duration) :

        s[n] = sound[n]*pow_ADSR(n,duration)

    return s

def pow_ADSR(pos,duration) :

    np = pos/duration

    if np < TADSR_A : return TADSR_DEPT * np / TADSR_A

    if np < TADSR_A + TADSR_D : return TADSR_DEPT - ( TADSR_DEPT - TADSR_S ) * ( np - TADSR_A ) / TADSR_D

    if np < 1.0 - TADSR_R : return TADSR_S

    return TADSR_S * (1.0 - np ) / TADSR_R

