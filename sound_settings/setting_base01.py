import numpy as np
from sound_base.color.sound_color import sound_string

#
# DISTORTION SETTING
#

gain = 1000
level = 0.5

#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    s0 = sound_string(sound_a,duration,note,sampling)

    s1 = sound_string(sound_a,duration,note-13*2,sampling)

    length_of_s_master = int(duration)

    sound_master = np.zeros(length_of_s_master)

    for n in range(length_of_s_master) :
        sound_master[n] += 0.5*s0[n]
        sound_master[n] += 0.5*s1[n]

    return sound_master

#
# MAKING ENDS
#
