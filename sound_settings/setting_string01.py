import numpy as np

from sound_base.color.sound_color import sound_string
from sound_base.effect.sound_effector import limitter

#
# SOUND SETTINFG
#



#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    sound_master = sound_string(sound_a,duration,note,sampling)

    return limitter(sound_master)

#
# MAKING ENDS
#

  

