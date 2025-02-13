import numpy as np
from sound_base.color.sound_color import sin_freq_decay
from sound_base.touch.sound_touch_ADSR import set_touch_HARD
from sound_base.touch.sound_touch_ADSR import touch_ADSR

#
# BASE SOUND
#

decay = 5.0

pow1   = 1.0
freq1  = 1.0
decay1 = decay/4.0

pow2   = 0.5
freq2  = 2.8
decay2 = decay/1.0

pow3   = 0.3
freq3  = 5.4
decay3 = decay/0.8

pow4   = 0.2
freq4  = 8.9
decay4 = decay/0.6

pow5   = 0.1
freq5  = 13.3
decay5 = decay/0.5

pow6   = 0.1
freq6  = 18.6
decay6 = decay/0.54

pow7   = 0.1
freq7  = 24.8
decay7 = decay/0.5

#
# SET TOUCH
#

set_touch_HARD

#
# MAKE SOUNDS
#

def set_sound(note,sound_a,sampling,duration) :

    length_of_s_master = int(duration)
    s0 = np.zeros(length_of_s_master)

    s1 = sin_freq_decay(sound_a,duration,note,freq1,pow1,sampling,decay1)
    s2 = sin_freq_decay(sound_a,duration,note,freq2,pow2,sampling,decay2)
    s3 = sin_freq_decay(sound_a,duration,note,freq3,pow3,sampling,decay3)
    s4 = sin_freq_decay(sound_a,duration,note,freq4,pow4,sampling,decay4)
    s5 = sin_freq_decay(sound_a,duration,note,freq5,pow5,sampling,decay5)
    s6 = sin_freq_decay(sound_a,duration,note,freq6,pow6,sampling,decay6)
    s7 = sin_freq_decay(sound_a,duration,note,freq7,pow7,sampling,decay7)

    for n in range(length_of_s_master):
        if n>= duration : break
        s0[n] += s1[n]
        s0[n] += s2[n]
        s0[n] += s3[n]
        s0[n] += s4[n]
        s0[n] += s5[n]
        s0[n] += s6[n]
        s0[n] += s7[n]

    sound_master = touch_ADSR(s0)

    sound_master /= np.max(np.abs(sound_master))

    return sound_master
#
# MAKING ENDS
#


