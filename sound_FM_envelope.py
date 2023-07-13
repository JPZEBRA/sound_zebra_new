import numpy as np

FME_L1 = 100
FME_L2 = 100
FME_L3 = 100
FME_L4 = 0

FME_A1 = 0
FME_A2 = 0
FME_A3 = 0
FME_A4 = 0

# SOUND LEVEL 0-100

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

def set_FME(sound):

    duration = len(sound)

    s = np.zeros(duration)

    mode = 0
    cts = 0
    count = duration

    level = FME_L4

    for n in range(duration) :

        s[n] = level/100
 
        if mode >= 3 :
            if n >= count : mode = 4
        else :
            cts = cts + 1
            if cts >= count :
                mode = mode + 1
                if mode == 1 : level = FME_L1
                if mode == 2 : level = FME_L2
                if mode == 3 : level = FME_L3
 
        if mode == 0 :
            if FME_A1 == 0 or FME_A1 >= 90 :
                mode == 1
                count = 0
                level = FME_L1
            else :
                level = level + np.sign(FME_L1 - FME_L4)*np.sin(np.pi*FME_A1/180)*100/duration
                count = int(np.abs(FME_L1 - FME_L4)/np.tan(np.pi*FME_A1/180))*duration/100
            continue
        if mode == 1 :
            if FME_A2 == 0 or FME_A2 >= 90 :
                mode == 2
                count = 0
                level = FME_L2
            else :
                level = level + np.sign(FME_L2 - FME_L1)*np.sin(np.pi*FME_A2/180)*100/duration
                count = int(np.abs(FME_L2 - FME_L1)/np.tan(np.pi*FME_A2/180))*duration/100
            continue
        if mode == 2 :
            if FME_A3 == 0 or FME_A3 >= 90 :
                mode == 3
                count = 0
                level = FME_L3
            else :
                level = level + np.sign(FME_L3 - FME_L2)*np.sin(np.pi*FME_A3/180)*100/duration
                count = int(np.abs(FME_L3 - FME_L2)/np.tan(np.pi*FME_A3/180))*duration/100
            continue
        if mode == 3 :
            if FME_A4 == 0 or FME_A4 >= 90 :
                count = duration
            else :
                count = duration - int(np.abs(FME_L4 - FME_L3)/np.tan(np.pi*FME_A4/180))*duration/100
            continue
        if mode == 4 :
                level = level - np.sign(FME_L4 - FME_L3)*np.sin(np.pi*FME_A4/180)*100/duration

    for n in range(duration) :

        s[n] = s[n]*sound[n]

    return s
