import numpy as np
from sound_base.color.sound_color import pulse_decay

#
# SOUND SETTING
#

decay = 10

#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    pow = 1.0

    sound_master = pulse_decay(sound_a,duration,note,pow,sampling,decay)
  
    return sound_master

#
# MAKING ENDS
#



