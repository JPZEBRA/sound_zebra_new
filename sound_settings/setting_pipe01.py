import numpy as np

from aoki_sound.musical_instruments import pipe_organ

#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    sound_master = pipe_organ(sampling,note,100,4)

    return sound_master

#
# MAKING ENDS
#

