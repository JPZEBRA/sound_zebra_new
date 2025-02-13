import numpy as np

from sound_base.color.sound_color import sound_string

#
# SOUND SETTINFG
#



#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    sound_master = sound_string(sound_a,duration,note,sampling)

    sound_master /= np.max(np.abs(sound_master))

    return sound_master

#
# MAKING ENDS
#

  

