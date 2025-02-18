# E-PIANO

import numpy as np

#
# SOUNDS LIB
#


from sound_base.color.sound_color import sin_out
from sound_base.color.sound_color import sin_freq_out
from sound_base.color.sound_color import pulse_out
from sound_base.color.sound_color import sawtooth_out
from sound_base.color.sound_color import sawtooth_freq_out

from sound_base.effect.sound_effector import limitter
from sound_base.effect.sound_effector import reverse
from sound_base.effect.sound_effector import LPFilter
from sound_base.effect.sound_effector import HPFilter

from sound_base.FM.sound_FM_envelope import set_FME_level
from sound_base.FM.sound_FM_envelope import set_FME_poly

from sound_base.FM.sound_FM_unit import SINNote
from sound_base.FM.sound_FM_unit import SINFreq
from sound_base.FM.sound_FM_unit import Freq
from sound_base.FM.sound_FM_unit import Mix
from sound_base.FM.sound_FM_unit import Modulate
from sound_base.FM.sound_FM_unit import Sync
from sound_base.FM.sound_FM_unit import SETEnv

#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    s1  = SINNote(sound_a,duration,note,1.0,0.0,sampling)

    s2  = sawtooth_out(sound_a,duration,note,1.0,sampling)
    s3  = pulse_out(sound_a,duration,note-12,0.5,1.0,sampling)

    e0  = SINNote(sound_a,duration,note-1,1.0,0.0,sampling)

    set_FME_level(100,50,30,0)
    set_FME_poly(75,70,50,30)

    e1 = SETEnv(e0,duration)

    s5 = Mix(s2,s3,0.5)

    s6 = Modulate(s5,e1,0.50,0.0)

    s7 = LPFilter(sampling,s6,Freq(sound_a,note+17),0.5,0.2)

    s8 = Mix(s1,s7,0.6) 


    set_FME_level(100,80,50,0)
    set_FME_poly(0,85,60,30)

    so = SETEnv(s8,duration)

    return limitter(so)

#
# MAKING ENDS
#
