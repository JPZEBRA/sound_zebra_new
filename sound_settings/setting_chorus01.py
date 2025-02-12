import numpy as np

from sound_base.color.sound_color_ADSR import set_ADSR_HARD
from sound_base.color.sound_color_ADSR import set_ADSR_GENTRE
from sound_base.color.sound_color_ADSR import set_ADSR_SOFT
from sound_base.color.sound_color_ADSR import set_ADSR_IDIOT

from sound_base.color.sound_color_ADSR import sawtooth_out_ADSR

from aoki.biquad_filter import LPF
from aoki.biquad_filter import filter

from sound_base.touch.sound_touch_ADSR import set_touch_GENTRE
from sound_base.touch.sound_touch_ADSR import touch_ADSR
from sound_base.touch.sound_touch_ADSR import delay

#
# FILTER SETTING
#

fcut = 1000

quality = 1/np.sqrt(2)

duration = 100000

#
# SOUND SETTINFG
#

set_ADSR_IDIOT

set_touch_GENTRE


#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :


    a,b = LPF(sampling,fcut,quality)
    pow = 1.0

    length_of_s_master = int(duration)
    sound_master = np.zeros(length_of_s_master)

    for dt in range(0,60) :
        st = sawtooth_out_ADSR(sound_a,duration,note + (dt % 20 - 10) /17 + np.random.rand()/3,pow,sampling)
        sk = touch_ADSR(st)
        sd = delay(sk,int(np.random.rand()*100))
        sf = filter(a,b,sd)
        sound_master += sf

    sound_master /= np.max(np.abs(sound_master))

    return sound_master

#
# MAKING ENDS
#

  

