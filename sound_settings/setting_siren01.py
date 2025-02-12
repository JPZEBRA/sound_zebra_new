import numpy as np

from sound_base.color.sound_color_ADSR import set_ADSR_HARD
from sound_base.color.sound_color_ADSR import set_ADSR_GENTRE
from sound_base.color.sound_color_ADSR import set_ADSR_SOFT
from sound_base.color.sound_color_ADSR import set_ADSR_IDIOT
from sound_base.color.sound_color_ADSR import sawtooth_out_ADSR
from aoki.biquad_filter import LPF
from aoki.biquad_filter import filter

from sound_base.touch.sound_touch_ADSR import set_touch_HARD
from sound_base.touch.sound_touch_ADSR import set_touch_GENTRE
from sound_base.touch.sound_touch_ADSR import set_touch_SOFT
from sound_base.touch.sound_touch_ADSR import touch_ADSR

#
# FILTER SETTING
#

fcut = 1000

quality = 1/np.sqrt(2)

#
# SET SOUND
#

set_ADSR_GENTRE()

set_touch_GENTRE()

#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    pow = 1.0

    s1 = sawtooth_out_ADSR(sound_a,duration,note,pow*0.8,sampling)
    s2 = sawtooth_out_ADSR(sound_a,duration,note+4,pow*0.4,sampling)
    s3 = sawtooth_out_ADSR(sound_a,duration,note+7,pow*0.2,sampling)

    s1t = touch_ADSR(s1)
    s2t = touch_ADSR(s2)
    s3t = touch_ADSR(s3)

    length_of_s_master = int(duration)
    sound_master = np.zeros(length_of_s_master)

    for n in range(length_of_s_master):
        if n>= duration : break
        sound_master[n] += s1t[n]
        sound_master[n] += s2t[n]
        sound_master[n] += s3t[n]

    sound_master /= np.max(np.abs(sound_master))

    a,b = LPF(sampling,fcut,quality)

    sound_filterd = filter(a,b,sound_master)

    return sound_filterd

#
# MAKING ENDS
#
