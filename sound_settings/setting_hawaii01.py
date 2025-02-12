import numpy as np
from sound_base.color.sound_color import sin_out
from sound_base.color.sound_color import sin_decay

#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    decay = 10
  
    s1 = sin_decay(sound_a,duration,note,0.8,sampling,decay)
    length_of_s = len(s1)
  
    s2 = sin_decay(sound_a,duration,note+4,0.4,sampling,decay)

    s3 = sin_decay(sound_a,duration,note+7,0.2,sampling,decay)

    length_of_s_master = int(duration)
    sound_master = np.zeros(length_of_s_master)

    for n in range(length_of_s):
        if n>= duration : break
        sound_master[n] += s1[n]
        sound_master[n] += s2[n]
        sound_master[n] += s3[n]

    return sound_master

#
# MAKING ENDS
#
