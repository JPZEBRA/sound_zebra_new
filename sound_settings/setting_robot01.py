import numpy as np
from sound_base.color.sound_color import pulse_decay
from sound_base.color.sound_color import color_noise

#
# SOUND SETTING
#

decay = 0.7
ratio = 0.3

pow = 1.0

#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    s0 = pulse_decay(sound_a,duration,note,ratio,decay,pow,sampling)
    sn = color_noise(sound_a,duration,note,sampling)
 
    s1 = np.zeros(duration)

    for n in range (0,5) :
        len = duration
        blk = int(duration / 10)
        for i in range(0,len) :
            if blk*n + i >= duration : break
            s1[blk*n+i] = s0[i]

    sound_master = s1 * 0.7 + sn * 0.3
 
    return sound_master

#
# MAKING ENDS
#



