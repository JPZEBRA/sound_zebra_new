import numpy as np
from sound_base.color.sound_color import FM_out

#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    ratio = 1.012

    pow = 1.0

    pow_m = 1.0

    sound_master = FM_out(sound_a,duration,note,pow,ratio,pow_m,sampling)

    return sound_master

#
# MAKING ENDS
#

