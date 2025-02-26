import numpy as np

FME_L1 = 100
FME_L2 = 100
FME_L3 = 100
FME_L4 = 0

FME_A1 = 0
FME_A2 = 0
FME_A3 = 0
FME_A4 = 0

FME_C1 = 0.002

###################
# PRESET ENVELOPE #
###################

def set_FME_tone() :

    set_FME_level(100,100,100,  0)
    set_FME_poly (  0,  0,  0,  0)

def set_FME_grow() :

    set_FME_level(  0,  0,  0,100)
    set_FME_poly (  0,  0,  0, 20)

def set_FME_organ() :

    set_FME_level(100,100,100,  0)
    set_FME_poly ( 85,  0,  0,  0)

def set_FME_decay() :

    set_FME_level(100, 90, 50,  0)
    set_FME_poly (  0, 80, 50, 30)

def set_FME_gentle() :

    set_FME_level(100, 80, 60,  0)
    set_FME_poly ( 88, 85, 60, 10)

def set_FME_solid() :

    set_FME_level(100,  0,  0,  0)
    set_FME_poly (  0, 40,  0,  0)

def set_FME_hard() :

    set_FME_level(100,  0,  0,  0)
    set_FME_poly (  0, 60,  0,  0)

def set_FME_hard_remain() :

    set_FME_level(100, 20, 10,  0)
    set_FME_poly (  0, 60,  5,  5)

def set_FME_hard_long() :

    set_FME_level(100, 60, 30,  0)
    set_FME_poly (  0, 80, 20, 10)

def set_FME_very_hard() :

    set_FME_level(100,  0,  0,  0)
    set_FME_poly (  0, 80,  0,  0)

def set_FME_very_hard_remain() :

    set_FME_level(100, 20,  5,  0)
    set_FME_poly (  0, 80, 20,  5)

def set_FME_attack() :

    set_FME_level(100,  0,  0,  0)
    set_FME_poly (  0, 88,  0,  0)

def set_FME_attack_gentle() :

    set_FME_level(100,  0,  0,  0)
    set_FME_poly ( 80, 70,  0,  0)

def set_FME_slow() :

    set_FME_level(100, 90, 50,  0)
    set_FME_poly ( 70, 80, 50, 30)


###########
# SETTING #
###########

def set_FME(sound,duration):

    s = set_Envelope(duration,1.0)

    so = s * sound

    return so

#####################
# SOUND LEVEL 0-100 #
#####################

def set_FME_level(L1,L2,L3,L4) :

    global FME_L1
    global FME_L2
    global FME_L3
    global FME_L4

    FME_L1 = L1
    FME_L2 = L2
    FME_L3 = L3
    FME_L4 = L4

# SOUND ANGLE 0-90

def set_FME_poly(A1,A2,A3,A4) :

    global FME_A1
    global FME_A2
    global FME_A3
    global FME_A4

    FME_A1 = A1
    FME_A2 = A2
    FME_A3 = A3
    FME_A4 = A4

def set_FME_speed(speed,sampling) :

    global FME_C1

    FME_C1 = 0.002 * 441000 / sampling

########
# MAIN #
########

def set_Envelope(duration,amount):

    s = np.zeros(duration)

    count = [0,0,0,0,0]

    if FME_A1== 0 or FME_A1>= 90 :
        count[0] = 0
    else :
        count[0] = int(np.abs(FME_L1 - FME_L4)/np.tan(np.pi*FME_A1/180))/FME_C1
    if FME_A2 == 0 or FME_A2 >= 90 :
        count[1] = count[0]
    else :
        count[1] = count[0] + int(np.abs(FME_L2 - FME_L1)/np.tan(np.pi*FME_A2/180))/FME_C1
    if FME_A3 == 0 or FME_A3 >= 90 :
        count[2] = count[1]
    else :
        count[2] = count[1] + int(np.abs(FME_L3 - FME_L2)/np.tan(np.pi*FME_A3/180))/FME_C1
    if FME_A4 == 0 or FME_A4 >= 90 :
        count[3] = duration
    else :
        count[3] = duration - int(np.abs(FME_L4 - FME_L3)/np.tan(np.pi*FME_A4/180))/FME_C1

    count[4] = duration

    level = FME_L4

    mode = 0

    if FME_A1 == 0 or FME_A1 >= 90 : level = FME_L1

    for n in range(duration) :

        s[n] = level/100

        if n >= count[mode] : mode = mode + 1

        if mode == 0 :
            if( count[0] > 0 ) :
                level = (FME_L1 - FME_L4)/ count[0] * n + FME_L4
            else :
                mode = mode + 1
        if mode == 1 :
            if( count[1] - count[0] > 0 ) :
                level = (FME_L2 - FME_L1)/(count[1]-count[0]) * ( n - count[0]) + FME_L1
            else :
                mode = mode + 1
        if mode == 2 :
            if( count[2] - count[1] > 0 ) :
                level = (FME_L3 - FME_L2)/(count[2]-count[1]) * ( n - count[1]) + FME_L2
            else :
                mode = mode + 1
        if mode == 4 :
            if( count[4] - count[3] > 0 ) :
                level = (FME_L4 - FME_L3)/(count[4]-count[3]) * ( n - count[3]) + FME_L3
            else :
                mode = mode + 1
        if mode == 5 :
            level = FME_L4

    so = s * amount

    return so

