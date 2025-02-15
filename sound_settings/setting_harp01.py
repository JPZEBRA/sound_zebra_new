import numpy as np

from aoki_sound.musical_instruments import harpsichord

#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    sound_master = harpsichord(sampling,note,100,4)

    return sound_master

#
# MAKING ENDS
#

