import numpy as np
from sound_base.color.sound_color import sound_noisy
from sound_base.touch.sound_touch_ADSR import set_touch_HARD
from sound_base.touch.sound_touch_ADSR import touch_ADSR

#
# BASE SOUND
#

decay = 5.0

pow1   = 1.0
freq1  = 1.0

pow2   = 1.0
freq2  = 4.0

pow3   = 1.0
freq3  = 10.0

#
# SET TOUCH
#

set_touch_HARD()

#
# MAKE SOUNDS
#

def set_sound(note,sound_a,sampling,duration) :

    length_of_s_master = int(duration)

    s0 = np.zeros(length_of_s_master)

    s1 = sound_noisy(sound_a,duration,note,freq1,sampling)
    s2 = sound_noisy(sound_a,duration,note,freq2,sampling)
    s3 = sound_noisy(sound_a,duration,note,freq3,sampling)

    for n in range(length_of_s_master):
        if n>= duration : break
        s0[n] += pow1 * s1[n]
        s0[n] += pow2 * s2[n]
        s0[n] += pow3 * s3[n]

    sound_master = touch_ADSR(s0)

    sound_master /= np.max(np.abs(sound_master))

    return sound_master
#
# MAKING ENDS
#


