import numpy as np

from sound_base.color.sound_color import sin_decay

#
# SOUND SETTINFG
#

decay = 10

#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    sound_master = sin_decay(sound_a,duration,note,1.0,sampling,decay)

    sound_master /= np.max(np.abs(sound_master))

    return sound_master

#
# MAKING ENDS
#

  

