import numpy as np

TADSR_Z = 0.00
TADSR_A = 0.01
TADSR_D = 0.10
TADSR_S = 1.00
TADSR_R = 0.30
TADSR_DEPT = 1.05

def set_touch_ADSR(delay,attack,duration,sustain,reduce,depth) :

    global TADSR_Z
    global TADSR_A
    global TADSR_D
    global TADSR_S
    global TADSR_R
    global TADSR_DEPT

    TADSR_Z = delay
    TADSR_A = attack
    TADSR_D = duration
    TADSR_S = sustain
    TADSR_R = reduce
    TADSR_DEPT = depth

def set_touch_HARD() :

    global TADSR_Z
    global TADSR_A
    global TADSR_D
    global TADSR_S
    global TADSR_R
    global TADSR_DEPT

    TADSR_Z = 0.00
    TADSR_A = 0.01
    TADSR_D = 0.20
    TADSR_S = 0.30
    TADSR_R = 0.50
    TADSR_DEPT = 2.00

def set_touch_GENTRE() :

    global TADSR_Z
    global TADSR_A
    global TADSR_D
    global TADSR_S
    global TADSR_R
    global TADSR_DEPT

    TADSR_Z = 0.00
    TADSR_A = 0.30
    TADSR_D = 0.30
    TADSR_S = 1.00
    TADSR_R = 0.10
    TADSR_DEPT = 1.01

def set_touch_SOFT() :

    global TADSR_Z
    global TADSR_A
    global TADSR_D
    global TADSR_S
    global TADSR_R
    global TADSR_DEPT

    TADSR_Z = 0.00
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

    return delay(s,int(TADSR_Z * duration))

def delay(sound,pos) :

    duration = len(sound)

    s = np.zeros(duration)

    for n in range(duration) :

        if n - pos >= 0 :

            s[n] = sound[n - pos]

        else :

            s[n] = 0

    return s

def pow_ADSR(pos,duration) :

    nps = pos/duration

    if nps < TADSR_A : return TADSR_DEPT * ( nps - 0 ) / TADSR_A

    if nps < TADSR_A + TADSR_D : return TADSR_DEPT - ( TADSR_DEPT - TADSR_S ) * ( nps - TADSR_A ) / TADSR_D

    if nps < 1.0 - TADSR_R : return TADSR_S

    return TADSR_S * (1.0 - nps ) / TADSR_R

