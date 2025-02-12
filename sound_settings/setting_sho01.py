import numpy as np
from sound_base.color.sound_color_ADSR import sin_out_ADSR
from sound_base.color.sound_color_ADSR import set_ADSR_BRASS


#
# BASE SOUND
#

octave = 2

i = 0

note = ( octave + 1 ) * 12 - 3 + ( i - 8)

#
# SET TOUCH
#

set_ADSR_BRASS()

#
# MAKE SOUNDS
#

def set_sho001(note,sound_a,sampling,duration) :

    s1 = sin_out_ADSR(sound_a,duration,note-5,0.13,sampling)

    length_of_s = len(s1)
  
    s2 = sin_out_ADSR(sound_a,duration,note+0,0.13,sampling)

    s3 = sin_out_ADSR(sound_a,duration,note+2,0.13,sampling)

    s4 = sin_out_ADSR(sound_a,duration,note+5,0.13,sampling)

    s5 = sin_out_ADSR(sound_a,duration,note+7,0.13,sampling)

    s6 = sin_out_ADSR(sound_a,duration,note+9,0.13,sampling)

    length_of_s_master = int(duration)
    sound_master = np.zeros(length_of_s_master)

    for n in range(length_of_s):
        if n>= duration : break
        sound_master[n] += s1[n]
        sound_master[n] += s2[n]
        sound_master[n] += s3[n]
        sound_master[n] += s4[n]
        sound_master[n] += s5[n]
        sound_master[n] += s6[n]

    return sound_master

def set_sho002(note,sound_a,sampling,duration) :

    s1 = sin_out_ADSR(sound_a,duration,note-5,0.13,sampling)

    length_of_s = len(s1)
  
    s2 = sin_out_ADSR(sound_a,duration,note+0,0.13,sampling)

    s3 = sin_out_ADSR(sound_a,duration,note+2,0.13,sampling)

    s4 = sin_out_ADSR(sound_a,duration,note-7,0.13,sampling)

    s5 = sin_out_ADSR(sound_a,duration,note+7,0.13,sampling)

    s6 = sin_out_ADSR(sound_a,duration,note+9,0.13,sampling)


    length_of_s_master = int(duration)
    sound_master = np.zeros(length_of_s_master)

    for n in range(length_of_s):
        if n>= duration : break
        sound_master[n] += s1[n]
        sound_master[n] += s2[n]
        sound_master[n] += s3[n]
        sound_master[n] += s4[n]
        sound_master[n] += s5[n]
        sound_master[n] += s6[n]

    return sound_master

def set_sho003(note,sound_a,sampling,duration) :

    s1 = sin_out_ADSR(sound_a,duration,note-5,0.13,sampling)

    length_of_s = len(s1)

    s2 = sin_out_ADSR(sound_a,duration,note+0,0.13,sampling)

    s3 = sin_out_ADSR(sound_a,duration,note+2,0.13,sampling)

    s4 = sin_out_ADSR(sound_a,duration,note-7,0.13,sampling)

    s5 = sin_out_ADSR(sound_a,duration,note-10,0.13,sampling)

    s6 = sin_out_ADSR(sound_a,duration,note+9,0.13,sampling)


    length_of_s_master = int(duration)
    sound_master = np.zeros(length_of_s_master)

    for n in range(length_of_s):
        if n>= duration : break
        sound_master[n] += s1[n]
        sound_master[n] += s2[n]
        sound_master[n] += s3[n]
        sound_master[n] += s4[n]
        sound_master[n] += s5[n]
        sound_master[n] += s6[n]

    return sound_master

def set_sho004(note,sound_a,sampling,duration) :

    s1 = sin_out_ADSR(sound_a,duration,note-5,0.13,sampling)

    length_of_s = len(s1)

    s2 = sin_out_ADSR(sound_a,duration,note+0,0.13,sampling)

    s3 = sin_out_ADSR(sound_a,duration,note+2,0.13,sampling)

    s4 = sin_out_ADSR(sound_a,duration,note+5,0.13,sampling)

    s5 = sin_out_ADSR(sound_a,duration,note-12,0.13,sampling)

    s6 = sin_out_ADSR(sound_a,duration,note+9,0.13,sampling)


    length_of_s_master = int(duration)
    sound_master = np.zeros(length_of_s_master)

    for n in range(length_of_s):
        if n>= duration : break
        sound_master[n] += s1[n]
        sound_master[n] += s2[n]
        sound_master[n] += s3[n]
        sound_master[n] += s4[n]
        sound_master[n] += s5[n]
        sound_master[n] += s6[n]

    return sound_master

def set_sho005(note,sound_a,sampling,duration) :

    s1 = sin_out_ADSR(sound_a,duration,note+0,0.13,sampling)

    length_of_s = len(s1)

    s2 = sin_out_ADSR(sound_a,duration,note+2,0.13,sampling)

    s3 = sin_out_ADSR(sound_a,duration,note+5,0.13,sampling)

    s4 = sin_out_ADSR(sound_a,duration,note+7,0.13,sampling)

    s5 = sin_out_ADSR(sound_a,duration,note+9,0.13,sampling)

    length_of_s_master = int(duration)
    sound_master = np.zeros(length_of_s_master)

    for n in range(length_of_s):
        if n>= duration : break
        sound_master[n] += s1[n]
        sound_master[n] += s2[n]
        sound_master[n] += s3[n]
        sound_master[n] += s4[n]
        sound_master[n] += s5[n]

    return sound_master

def set_sho006(note,sound_a,sampling,duration) :

    s1 = sin_out_ADSR(sound_a,duration,note-4,0.13,sampling)

    length_of_s = len(s1)

    s2 = sin_out_ADSR(sound_a,duration,note-1,0.13,sampling)

    s3 = sin_out_ADSR(sound_a,duration,note+0,0.13,sampling)

    s4 = sin_out_ADSR(sound_a,duration,note+2,0.13,sampling)

    s5 = sin_out_ADSR(sound_a,duration,note+5,0.13,sampling)

    s6 = sin_out_ADSR(sound_a,duration,note+7,0.13,sampling)

    length_of_s_master = int(duration)
    sound_master = np.zeros(length_of_s_master)

    for n in range(length_of_s):
        if n>= duration : break
        sound_master[n] += s1[n]
        sound_master[n] += s2[n]
        sound_master[n] += s3[n]
        sound_master[n] += s4[n]
        sound_master[n] += s5[n]
        sound_master[n] += s6[n]

    return sound_master

def set_sho007(note,sound_a,sampling,duration) :

    s1 = sin_out_ADSR(sound_a,duration,note-1,0.13,sampling)

    length_of_s = len(s1)

    s2 = sin_out_ADSR(sound_a,duration,note+0,0.13,sampling)

    s3 = sin_out_ADSR(sound_a,duration,note+2,0.13,sampling)

    s4 = sin_out_ADSR(sound_a,duration,note+5,0.13,sampling)

    s5 = sin_out_ADSR(sound_a,duration,note+7,0.13,sampling)

    length_of_s_master = int(duration)
    sound_master = np.zeros(length_of_s_master)

    for n in range(length_of_s):
        if n>= duration : break
        sound_master[n] += s1[n]
        sound_master[n] += s2[n]
        sound_master[n] += s3[n]
        sound_master[n] += s4[n]
        sound_master[n] += s5[n]

    return sound_master

def set_sho008(note,sound_a,sampling,duration) :

    s1 = sin_out_ADSR(sound_a,duration,note-3,0.13,sampling)

    length_of_s = len(s1)

    s2 = sin_out_ADSR(sound_a,duration,note-1,0.13,sampling)

    s3 = sin_out_ADSR(sound_a,duration,note+1,0.13,sampling)

    s4 = sin_out_ADSR(sound_a,duration,note+2,0.13,sampling)

    s5 = sin_out_ADSR(sound_a,duration,note+5,0.13,sampling)

    s6 = sin_out_ADSR(sound_a,duration,note+9,0.13,sampling)

    length_of_s_master = int(duration)
    sound_master = np.zeros(length_of_s_master)

    for n in range(length_of_s):
        if n>= duration : break
        sound_master[n] += s1[n]
        sound_master[n] += s2[n]
        sound_master[n] += s3[n]
        sound_master[n] += s4[n]
        sound_master[n] += s5[n]
        sound_master[n] += s6[n]

    return sound_master

def set_sho009(note,sound_a,sampling,duration) :

    s1 = sin_out_ADSR(sound_a,duration,note-11,0.13,sampling)

    length_of_s = len(s1)

    s2 = sin_out_ADSR(sound_a,duration,note-9,0.13,sampling)

    s3 = sin_out_ADSR(sound_a,duration,note-8,0.13,sampling)

    s4 = sin_out_ADSR(sound_a,duration,note-4,0.13,sampling)

    s5 = sin_out_ADSR(sound_a,duration,note-2,0.13,sampling)

    s6 = sin_out_ADSR(sound_a,duration,note-1,0.13,sampling)

    length_of_s_master = int(duration)
    sound_master = np.zeros(length_of_s_master)

    for n in range(length_of_s):
        if n>= duration : break
        sound_master[n] += s1[n]
        sound_master[n] += s2[n]
        sound_master[n] += s3[n]
        sound_master[n] += s4[n]
        sound_master[n] += s5[n]
        sound_master[n] += s6[n]

    return sound_master

def set_sho010(note,sound_a,sampling,duration) :

    s1 = sin_out_ADSR(sound_a,duration,note-2,0.13,sampling)

    length_of_s = len(s1)

    s2 = sin_out_ADSR(sound_a,duration,note+1,0.13,sampling)

    s3 = sin_out_ADSR(sound_a,duration,note+2,0.13,sampling)

    s4 = sin_out_ADSR(sound_a,duration,note+3,0.13,sampling)

    s5 = sin_out_ADSR(sound_a,duration,note+5,0.13,sampling)

    s6 = sin_out_ADSR(sound_a,duration,note+10,0.13,sampling)


    length_of_s_master = int(duration)
    sound_master = np.zeros(length_of_s_master)

    for n in range(length_of_s):
        if n>= duration : break
        sound_master[n] += s1[n]
        sound_master[n] += s2[n]
        sound_master[n] += s3[n]
        sound_master[n] += s4[n]
        sound_master[n] += s5[n]
        sound_master[n] += s6[n]

    return sound_master

def set_sho011(note,sound_a,sampling,duration) :

    s1 = sin_out_ADSR(sound_a,duration,note+10,0.13,sampling)

    length_of_s = len(s1)

    s2 = sin_out_ADSR(sound_a,duration,note+0,0.13,sampling)

    s3 = sin_out_ADSR(sound_a,duration,note+2,0.13,sampling)

    s4 = sin_out_ADSR(sound_a,duration,note+3,0.13,sampling)

    s5 = sin_out_ADSR(sound_a,duration,note+5,0.13,sampling)

    s6 = sin_out_ADSR(sound_a,duration,note+7,0.13,sampling)

    length_of_s_master = int(duration)
    sound_master = np.zeros(length_of_s_master)

    for n in range(length_of_s):
        if n>= duration : break
        sound_master[n] += s1[n]
        sound_master[n] += s2[n]
        sound_master[n] += s3[n]
        sound_master[n] += s4[n]
        sound_master[n] += s5[n]
        sound_master[n] += s6[n]

    return sound_master

#
# MAIN FUCTION
#

def set_sound(tone,sound_a,sampling,duration) :

    if(tone== 1) : return set_sho001(note,sound_a,sampling,duration)
    if(tone== 2) : return set_sho002(note,sound_a,sampling,duration)
    if(tone== 3) : return set_sho003(note,sound_a,sampling,duration)
    if(tone== 4) : return set_sho004(note,sound_a,sampling,duration)
    if(tone== 5) : return set_sho005(note,sound_a,sampling,duration)
    if(tone== 6) : return set_sho006(note,sound_a,sampling,duration)
    if(tone== 7) : return set_sho007(note,sound_a,sampling,duration)
    if(tone== 8) : return set_sho008(note,sound_a,sampling,duration)
    if(tone== 9) : return set_sho009(note,sound_a,sampling,duration)
    if(tone==10) : return set_sho010(note,sound_a,sampling,duration)
    if(tone==11) : return set_sho011(note,sound_a,sampling,duration)

#
# MAKING ENDS
#


