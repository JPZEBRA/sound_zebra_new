# FM PRESET

import numpy as np

from sound_base.color.sound_color import square_freq_out
from sound_base.effect.sound_effector import limitter
from sound_base.effect.sound_effector import fourier_power

from sound_base.FM.sound_FM_unit import SINNote
from sound_base.FM.sound_FM_unit import COSNote
from sound_base.FM.sound_FM_unit import SINFreq
from sound_base.FM.sound_FM_unit import COSFreq
from sound_base.FM.sound_FM_unit import SINFreqPitch
from sound_base.FM.sound_FM_unit import COSFreqPitch
from sound_base.FM.sound_FM_unit import Freq

#
# SOUND SETTING
#

FM_PRE_NM = 20
FM_PRE_PW =  1
FM_PRE_FQ = np.array([ 0.50, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 4.50, 5.00, 5.50, 6.00, 6.50, 7.00, 7.50, 8.00, 8.50, 9.00, 9.50,10.00])
FM_PRE_PS = np.array([    0,    1,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0])
FM_PRE_PC = np.array([    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0])
FM_PRE_BI = np.array([    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0])

################
# PRESET SOUND #
################

def FM_pre_sound(note,sound_a,sampling,duration) :

    return FM_pre_sound_f(Freq(sound_a,note),sound_a,sampling,duration)

def FM_pre_sound_f(freq,sound_a,sampling,duration) :

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    so = np.zeros(duration)

    for n in range(FM_PRE_NM) :

        pw = FM_PRE_PS[n] * FM_PRE_PS[n] + FM_PRE_PC[n] * FM_PRE_PC[n]

        if pw > 0 :

            so += FM_PRE_PS[n] * SINFreq(sound_a,duration,freq,FM_PRE_FQ[n],0.0,sampling) + FM_PRE_BI[n]
            so += FM_PRE_PC[n] * COSFreq(sound_a,duration,freq,FM_PRE_FQ[n],0.0,sampling) + FM_PRE_BI[n]

    so *= FM_PRE_PW

    return limitter(so)

def FM_pre_sound_pitch(note,sound_a,pitch,sampling,duration) :

    return FM_pre_sound_pitch_f(Freq(sound_a,note),pitch,sampling,duration)

def FM_pre_sound_pitch_f(freq,pitch,sampling,duration) :

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    so = np.zeros(duration)

    for n in range(FM_PRE_NM) :

        so += FM_PRE_PS[n] * SINFreqPitch(duration,freq,pitch,FM_PRE_FQ[n],0.0,sampling)
        so += FM_PRE_PC[n] * COSFreqPitch(duration,freq,pitch,FM_PRE_FQ[n],0.0,sampling)
        so += FM_PRE_BI[n]

    so *= FM_PRE_PW

    return limitter(so)

def FM_pre_sound_square(note,sound_a,sampling,duration) :

    return FM_pre_sound_square_f(Freq(sound_a,note),sound_a,sampling,duration)

def FM_pre_sound_square_f(freq,sound_a,sampling,duration) :

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    so = np.zeros(duration)

    for n in range(FM_PRE_NM) :

        pw = FM_PRE_PS[n] * FM_PRE_PS[n] + FM_PRE_PC[n] * FM_PRE_PC[n]

        if pw > 1 :

            so += np.sqrt(pw) * square_freq_out(sound_a,duration,freq * FM_PRE_FQ[n],1.0,sampling) + FM_PRE_BI[n]

    so *= FM_PRE_PW

    return limitter(so)

# BOOST POWER

def FM_pre_boost(power):

    global FM_PRE_NM
    global FM_PRE_PS
    global FM_PRE_PC

    for i in range(0,FM_PRE_NM) :
        if(i<len(power)) :
            FM_PRE_PS[i] = FM_PRE_PS[i] * power[i]
            FM_PRE_PC[i] = FM_PRE_PC[i] * power[i]


# SIN WAVE

def FM_pre_sin() :

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM = 20
    FM_PRE_PW = 1
    FM_PRE_FQ = np.array([ 0.50, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 4.50, 5.00, 5.50, 6.00, 6.50, 7.00, 7.50, 8.00, 8.50, 9.00, 9.50,10.00])
    FM_PRE_PS = np.array([    0,    1,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0])
    FM_PRE_PC = np.array([    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0])
    FM_PRE_BI = np.array([    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0])

def FM_pre_square() :

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM = 20
    FM_PRE_PW = 382
    FM_PRE_FQ = np.array([ 0.50, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 4.50, 5.00, 5.50, 6.00, 6.50, 7.00, 7.50, 8.00, 8.50, 9.00, 9.50,10.00])
    FM_PRE_PS = np.array([    0,  100,    0,    0,    0,   33,    0,    0,    0,   19,    0,    0,    0,   14,    0,    0,    0,   11,    0,    0])
    FM_PRE_PC = np.array([    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0])
    FM_PRE_BI = np.array([ 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50])

def FM_pre_pulse066() :

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM = 20
    FM_PRE_PW = 293
    FM_PRE_FQ = np.array([ 0.50, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 4.50, 5.00, 5.50, 6.00, 6.50, 7.00, 7.50, 8.00, 8.50, 9.00, 9.50,10.00])
    FM_PRE_PS = np.array([    0,  100,    0,   46,    0,    9,    0,   26,    0,   17,    0,    0,    0,   16,    0,    9,    0,    0,    0,   11])
    FM_PRE_PC = np.array([    0,  -54,    0,   29,    0,    0,    0,  -12,    0,   12,    0,   -2,    0,   -6,    0,    8,    0,   -2,    0,   -3])
    FM_PRE_BI = np.array([ 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66])

def FM_pre_pulse077() :

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM = 20
    FM_PRE_PW = 189
    FM_PRE_FQ = np.array([ 0.50, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 4.50, 5.00, 5.50, 6.00, 6.50, 7.00, 7.50, 8.00, 8.50, 9.00, 9.50,10.00])
    FM_PRE_PS = np.array([    0,   88,    0,   99,    0,   45,    0,    3,    0,    8,    0,   29,    0,   25,    0,    5,    0,    1,    0,   13])
    FM_PRE_PC = np.array([    0, -100,    0,  -12,    0,   31,    0,   12,    0,  -16,    0,  -11,    0,    9,    0,   10,    0,   -4,    0,   -9])
    FM_PRE_BI = np.array([ 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66])

def FM_pre_saw() :

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM = 20
    FM_PRE_PW = 191
    FM_PRE_FQ = np.array([ 0.50, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 4.50, 5.00, 5.50, 6.00, 6.50, 7.00, 7.50, 8.00, 8.50, 9.00, 9.50,10.00])
    FM_PRE_PS = np.array([    0, -100,    0,  -50,    0,  -33,    0,  -25,    0,  -19,    0,  -16,    0,  -14,    0,  -12,    0,  -11,    0,  -10])
    FM_PRE_PC = np.array([    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0])
    FM_PRE_BI = np.array([ 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00])


def FM_pre_tri() :

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM = 20
    FM_PRE_PW = 243
    FM_PRE_FQ = np.array([ 0.50, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 4.50, 5.00, 5.50, 6.00, 6.50, 7.00, 7.50, 8.00, 8.50, 9.00, 9.50,10.00])
    FM_PRE_PS = np.array([    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0])
    FM_PRE_PC = np.array([    0, -100,    0,    0,    0,  -11,    0,    0,    0,   -4,    0,    0,    0,   -2,    0,    0,    0,   -1,    0,    0])
    FM_PRE_BI = np.array([ 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00])

def FM_pre_suzu() :

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

#   FM_PRE_NM = 20
#   FM_PRE_PW = 0.1

#   FM_PRE_FQ = np.array([ 0.50, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 4.50, 5.00, 5.50, 6.00, 6.50, 7.00, 7.50, 8.00, 8.50, 9.00, 9.50,10.00])
#   FM_PRE_PS = np.array([    1,   71,   -2,    2,    0,    4,   -1,    0,    0,    1,    0,   -6,   -1,    0,    4,  -18,    0,  -12,   -6,  -20])
#   FM_PRE_PC = np.array([   -2, -100,   -5,   -5,   -2,    5,    2,   -1,   -1,    0,    0,    1,   -4,    0,   -6,   -3,    2,  -16,   -6,  -49])
#   FM_PRE_BI = np.array([ 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00])

    FM_PRE_NM = 4
    FM_PRE_PW = 0.1

    FM_PRE_FQ = np.array([ 1.00, 8.00, 9.00,10.00])
    FM_PRE_PS = np.array([   71,  -18,  -12,  -20])
    FM_PRE_PC = np.array([ -100,   -3,  -16,  -49])
    FM_PRE_BI = np.array([ 0.00, 0.00, 0.00, 0.00])

def FM_pre_guitar() :

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM =  6
    FM_PRE_PW =  1

    FM_PRE_FQ = np.array([ 1.00, 2.00, 3.00, 4.00, 5.00, 6.00])
    FM_PRE_PS = np.array([ -301, 1394, -393,   68,    9,   26])
    FM_PRE_PC = np.array([ -595,-1631,  289,   37,   10,  -18])
    FM_PRE_BI = np.array([ 0.00, 0.00, 0.00, 0.00, 0.00, 0.00])

def FM_pre_church() :

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM =  9
    FM_PRE_PW = 10

    FM_PRE_FQ = np.array([ 0.500, 0.750, 1.000, 1.750, 2.500, 2.750, 3.000, 3.750, 4.750])
    FM_PRE_PS = np.array([   122,   -98,  -160,  -188,    14,    98,    19,   -92,    28])
    FM_PRE_PC = np.array([   -62,   103,  -133,   -75,   -22,    11,     2,     2,    -9])
    FM_PRE_BI = np.array([  0.00,  0.00,  0.00,  0.00,  0.00,  0.00,  0.00,  0.00,  0.00])

def FM_pre_drum() :

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM = 15
    FM_PRE_PW =  1
    FM_PRE_FQ = np.array([ 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 4.50, 5.00, 5.50, 6.50, 7.00, 8.00, 8.50, 9.00])
    FM_PRE_PS = np.array([ 1059,  128,    3,  -78,  -12,   20,  -19,    0,  -23,   31,  -13,  -26,    8,    4,  -32])
    FM_PRE_PC = np.array([ -949,   30,  118, -157, -111,  -47,  -27,   21,   35,  -28,   34,   10,  -15,   20,   18])
    FM_PRE_BI = np.array([ 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00])

def FM_pre_vocal() :

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM =  7
    FM_PRE_PW =  1
    FM_PRE_FQ = np.array([ 1.00, 2.00, 3.00, 3.50, 4.50, 5.50, 6.50])
    FM_PRE_PS = np.array([   59,  375,   28,   -9,    2,   31,   17])
    FM_PRE_PC = np.array([ -635,  601,  508,   20,  -32,  -21,   53])
    FM_PRE_BI = np.array([ 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00])

def FM_pre_honk() :

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM =  8
    FM_PRE_PW =  1
    FM_PRE_FQ = np.array([ 1.00, 1.25, 2.00, 2.50, 3.00, 4.00, 5.00, 6.00])
    FM_PRE_PS = np.array([    0,   80,  -40,  -30,    0,   10,   10,  -40])
    FM_PRE_PC = np.array([  315, -280,  -70,    0,  -20,  -40,   53,  -30])
    FM_PRE_BI = np.array([ 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00])

def FM_pre_rghorn() :

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM = 10
    FM_PRE_PW =  1

    FM_PRE_FQ = np.array([ 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00,10.00])
    FM_PRE_PS = np.array([-2200, 1100,-1900, -240,  -60,  120, -150,  -60,  -20,  -30])
    FM_PRE_PC = np.array([  980,  960,  940,  440, -220,  -70,  230,   60, -100,  -60])
    FM_PRE_BI = np.array([ 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00])

def FM_pre_flute() :

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM =  2
    FM_PRE_PW =  0.50

    FM_PRE_FQ = np.array([ 1.00, 2.00])
    FM_PRE_PS = np.array([  100,   10])
    FM_PRE_PC = np.array([    0,    0])
    FM_PRE_BI = np.array([ 0.00, 0.00])

def FM_pre_oboe() :

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM =  5
    FM_PRE_PW =  0.95

    FM_PRE_FQ = np.array([ 1.00, 2.00, 3.00, 4.00, 5.00])
    FM_PRE_PS = np.array([  100,   30,   35,   20,   15])
    FM_PRE_PC = np.array([    0,    0,    0,    0,    0])
    FM_PRE_BI = np.array([ 0.00, 0.00, 0.00, 0.00, 0.00])

def FM_pre_clarinet() :

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM =  5
    FM_PRE_PW =  0.85

    FM_PRE_FQ = np.array([ 1.00, 2.00, 3.00, 4.00, 5.00])
    FM_PRE_PS = np.array([  100,    8,   35,    0,   15])
    FM_PRE_PC = np.array([    0,    0,    0,    0,    0])
    FM_PRE_BI = np.array([ 0.00, 0.00, 0.00, 0.00, 0.00])

def FM_pre_trumpetA() :

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM =  6
    FM_PRE_PW =  1

    FM_PRE_FQ = np.array([ 1.00, 2.00, 3.00, 4.00, 5.00, 6.00])
    FM_PRE_PS = np.array([   45,   30,   27,   10,    5,    3])
    FM_PRE_PC = np.array([    0,    0,    0,    0,    0,    0])
    FM_PRE_BI = np.array([ 0.00, 0.00, 0.00, 0.00, 0.00, 0.00])

def FM_pre_trumpetB() :

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM =  6
    FM_PRE_PW =  1

    FM_PRE_FQ = np.array([ 1.00, 2.00, 3.00, 4.00, 5.00, 6.00])
    FM_PRE_PS = np.array([   45,   30,   27,   10,    5,    3])
    FM_PRE_PC = np.array([    0,    0,    0,    0,    0,    0])
    FM_PRE_BI = np.array([ 0.15, 0.12, 0.00, 0.00, 0.00, 0.00])

def FM_pre_cornetA() :

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM =  6
    FM_PRE_PW =  1

    FM_PRE_FQ = np.array([ 1.00, 2.00, 3.00, 4.00, 5.00, 6.00])
    FM_PRE_PS = np.array([   45,   30,   20,    7,    3,    2])
    FM_PRE_PC = np.array([    0,  0.1,  0.2,  0.3,  0.3,  0.3])
    FM_PRE_BI = np.array([ 0.00, 0.00, 0.00, 0.00, 0.00, 0.00])

    FM_pre_boost(np.array([1.05, 1.0, 0.9, 0.8, 0.8, 0.8]))

def FM_pre_cornetB() :

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM =  6
    FM_PRE_PW =  1

    FM_PRE_FQ = np.array([ 1.00, 2.00, 3.00, 4.00, 5.00, 6.00])
    FM_PRE_PS = np.array([   45,   30,   20,    7,    3,    2])
    FM_PRE_PC = np.array([    0,  0.1,  0.2,  0.3,  0.3,  0.3])
    FM_PRE_BI = np.array([ 0.08, 0.06, 0.00, 0.00, 0.00, 0.00])

    FM_pre_boost(np.array([1.05, 1.0, 0.9, 0.8, 0.8, 0.8]))

def FM_pre_tromboneA():

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM = 6
    FM_PRE_PW = 1

    FM_PRE_FQ = np.array([1.00, 2.00, 3.00, 4.00, 5.00, 6.00])

    # 太くて暗い倍音
    FM_PRE_PS = np.array([50, 35, 30, 12, 5, 3])

    # 重いアタック（位相をズラす）
    FM_PRE_PC = np.array([0.0, 0.15, 0.25, 0.35, 0.35, 0.35])

    # A は揺れなし
    FM_PRE_BI = np.array([0, 0, 0, 0, 0, 0])

    FM_pre_boost(np.array([1.3, 1.2, 1.0, 0.9, 0.8, 0.7]))

def FM_pre_tromboneB():

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM = 6
    FM_PRE_PW = 1

    FM_PRE_FQ = np.array([1.00, 2.00, 3.00, 4.00, 5.00, 6.00])

    FM_PRE_PS = np.array([50, 35, 30, 12, 5, 3])
    FM_PRE_PC = np.array([0.0, 0.15, 0.25, 0.35, 0.35, 0.35])

    # 息の揺れは深くて遅い（4Hz〜4.5Hz）
    FM_PRE_BI = np.array([0.15, 0.10, 0.00, 0.00, 0.00, 0.00])

    FM_pre_boost(np.array([1.3, 1.2, 1.0, 0.9, 0.8, 0.7]))

def FM_pre_hornA():

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM = 6
    FM_PRE_PW = 1

    FM_PRE_FQ = np.array([1.00, 2.00, 3.00, 4.00, 5.00, 6.00])

    # 暗くて丸い倍音（ホルンの本質）
    FM_PRE_PS = np.array([55, 25, 20,  8, 3, 2])
    # アタックは「ボワッ」→ 位相を大きくズラす
    FM_PRE_PC = np.array([0.0, 0.20, 0.30, 0.40, 0.40, 0.40])
    # A は揺れなし
    FM_PRE_BI = np.array([0, 0, 0, 0, 0, 0])

    FM_pre_boost(np.array([1.15, 1.05, 0.95, 0.85, 0.80, 0.75]))

def FM_pre_hornB():

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM = 6
    FM_PRE_PW = 1

    FM_PRE_FQ = np.array([1.00, 2.00, 3.00, 4.00, 5.00, 6.00])

    FM_PRE_PS = np.array([55, 25, 20,  8, 3, 2])
    FM_PRE_PC = np.array([0.0, 0.20, 0.30, 0.40, 0.40, 0.40])

    # 息の揺れだけ（極浅）
    FM_PRE_BI = np.array([0.04, 0.03, 0.00, 0.00, 0.00, 0.00])

    FM_pre_boost(np.array([1.15, 1.05, 0.95, 0.85, 0.80, 0.75]))

def FM_pre_tinpani_base():

    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM = 6
    FM_PRE_PW = 1

    FM_PRE_FQ = np.array([1.00, 1.59, 2.14, 2.30, 2.65, 3.16])
    FM_PRE_PS = np.array([  55,   28,   32,   10,    5,    3])
    FM_PRE_PC = np.array([   0,    0,    0,    0,    0,    0])
    FM_PRE_BI = np.array([0.00, 0.00, 0.00, 0.00, 0.00, 0.00])

def FM_pre_tinpaniA():

    global FM_PRE_PS

    FM_pre_tinpani_base()
    FM_pre_boost(np.array([0.6, 0.4, 0.3, 0.2, 0.1, 0.1]))

def FM_pre_tinpaniB():

    global FM_PRE_PS

    FM_pre_tinpani_base()
    FM_pre_boost(np.array([1.2, 1.0, 0.8, 0.5, 0.3, 0.1]))

def FM_pitch_tinpani(sampling,duration):

    curve = np.zeros(duration)
    for i in range(duration):
        t = i / sampling

        # 0〜0.02：少し上がる
        if t < 0.02:
            curve[i] = 1.0 + 0.0015 * (t / 0.02)   # +15 cent

        # 0.02〜0.05：下がる
        elif t < 0.05:
            curve[i] = 1.015 - 0.0030 * ((t - 0.02) / 0.03)  # -30 cent

        # 0.05〜：ゆっくり戻る
        else:
            curve[i] = 0.985 + 0.015 * (t - 0.05)

    return curve

def FM_pre_isekai_church():
    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM = 9
    FM_PRE_PW = 6.5

    # 非整数倍音（異世界感の源）
    FM_PRE_FQ = np.array([
        0.48,   # 低い金属共鳴
        0.75,   # 教会鐘の特徴
        1.00,   # 基本
        1.67,   # 5/3 に近いが少しズラす
        2.41,   # 12/5 付近
        2.93,   # ほぼ 3倍音だがズラす
        3.76,   # 高域の金属
        4.91,   # 異世界の倍音
        1.618   # ？
    ])

    # サイン成分（奇数倍音寄り）
    FM_PRE_PS = np.array([
        120, -90, -160, -180, 40, 95, -60, 30, 90
    ])

    # コサイン成分（位相をズラして金属感）
    FM_PRE_PC = np.array([
        -70, 110, -130, -80, -20, 15, 5, -12, 30
    ])

    # バイアス（DC成分はゼロ）
    FM_PRE_BI = np.zeros(FM_PRE_NM)

def FM_pre_moonbell():
    global FM_PRE_NM
    global FM_PRE_PW
    global FM_PRE_FQ
    global FM_PRE_PS
    global FM_PRE_PC
    global FM_PRE_BI

    FM_PRE_NM = 6
    FM_PRE_PW = 1.8

    # 透明で静かな金属倍音
    FM_PRE_FQ = np.array([
        0.75,   # 鈴の柔らかい胴鳴り
        1.00,   # 基本
        2.00,   # 2倍音（澄んだ響き）
        3.00,   # 3倍音（細い金属）
        4.00,   # 高域の透明感
        1.618   # 月光のような黄金比の揺らぎ
    ])

    # サイン成分（柔らかい金属）
    FM_PRE_PS = np.array([
        70, 100, 40, 20, 10, 25
    ])

    # コサイン成分（位相を少しズラして透明感）
    FM_PRE_PC = np.array([
        -10, 0, 0, 0, 0, 5
    ])

    FM_PRE_BI = np.zeros(FM_PRE_NM)

###########
# ANALYSE #
###########


def FM_pre_spectrum(sound,freq,num,sampling) :

    if freq <= 0 : return FM_pre_spectrum_search(sound,sampling)

    ps,pc,bi = fourier_power(sound,freq,2,num,sampling)

    pw = ps * ps + pc * pc
    mx = np.max(pw)
    if mx > 0.01 : mx = np.sqrt(mx)

    for n in range(num) : print( " F: " + pad((1.0 + n / 2 ),5,2) + " S: " + pad(ps[n],8,2) + " C: " + pad(pc[n],8,2) + " B: " + pad(bi[n],7,1) + " P: " + pad(mx,7,1) )


def FM_pre_spectrum_search(sound,sampling) :

    under =   50
    limit = 2100

    top_level  = 0
    top_freq   = 0
    area_level = 0
    area_freq  = 0

    for freq in range (under,limit+1) :

        ps,pc,bi = fourier_power(sound,freq,1,1,sampling)

        pw = ps * ps + pc * pc
        mx = np.max(pw)
        if mx > 0.01 : mx = np.sqrt(mx)

        if mx > top_level :
            top_level = mx
            top_freq  = freq

        if mx > area_level :
            area_level = mx
            area_freq  = freq

#       if mx >= 100 :
#            print(" >>>" + pad(freq,4,0) + " Hz  / " + pad(mx,8,1))

        if freq % 100 == 0 :
            print("TO " + pad(freq,4,0) + " Hz  / " + pad(area_level,8,2) + " / " + pad(area_freq,4,0) + " Hz")
            area_level = 0


    print("\nF: " + str(top_freq) + "LV: " + str(int(top_level*100)/100))




def pad(num,k,f) :

    fmt = "f";

    if f == 0 : fmt = ".0f"
    if f == 1 : fmt = ".1f"
    if f == 2 : fmt = ".2f"
    if f == 3 : fmt = ".3f"

    fmt = ">" + str(k) + fmt

    fmt = "{:" + fmt + "}"

    return fmt.format(num)

