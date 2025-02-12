import numpy as np
from sound_base.color.sound_color import sin_out
from aoki.biquad_filter import LPF
from aoki.biquad_filter import filter

#
# FILTER SETTING
#

fcut = 1200

quality = 1/np.sqrt(2)


#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    pow = 1.0

    s0 = sin_out(sound_a,duration,note,pow,sampling)

    a,b = LPF(sampling,fcut,quality)

    sound_master = filter(a,b,s0)
  
    return sound_master

#
# MAKING ENDS
#



