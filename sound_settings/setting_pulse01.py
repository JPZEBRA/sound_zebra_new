import numpy as np
from sound_base.color.sound_color import pulse_decay

#
# SOUND SETTING
#

decay = 10
ratio = 0.3

pow = 1.0

#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    sound_master = pulse_decay(sound_a,duration,note,ratio,decay,pow,sampling)
  
    return sound_master

#
# MAKING ENDS
#



