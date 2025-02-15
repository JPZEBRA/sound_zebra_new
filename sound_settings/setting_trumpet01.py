import numpy as np

from sound_base.brass.sound_brass import tone_brass_trumpet

#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    sound_master = tone_brass_trumpet(note,sound_a,sampling,duration)

    return sound_master

#
# MAKING ENDS
#

