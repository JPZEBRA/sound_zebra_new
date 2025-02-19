import numpy as np
from sound_base.color.sound_color import sawtooth_decay
from aoki.biquad_filter import LPF
from aoki.biquad_filter import filter

#
# SOUND SETTING
#

decay = 10

#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    pow = 1.0

    s1 = sawtooth_decay(sound_a,duration,note,pow,sampling,decay)

    cutoff = Freq(sound_a,note)

    amount = cutoff / 2.0

    level = 0.5

    env = set_Envelope(duration,amount):
 
    so = EGFilter(sampling,s1,cutoff,level,resonance,env) :
 
    return so

#
# MAKING ENDS
#



