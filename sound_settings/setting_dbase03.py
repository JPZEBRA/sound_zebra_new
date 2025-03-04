# SOLID BASE ( TEST008 )

import numpy as np

#
# SOUNDS LIB
#


from sound_base.color.sound_color import sin_out
from sound_base.color.sound_color import sin_freq_out
from sound_base.color.sound_color import sawtooth_out
from sound_base.color.sound_color import sawtooth_freq_out
from sound_base.color.sound_color import pulse_out

from sound_base.effect.sound_effector import limitter
from sound_base.effect.sound_effector import fourier_trans_ratio
from sound_base.effect.sound_effector import LPFilter
from sound_base.effect.sound_effector import EGFilter

from sound_base.FM.sound_FM_envelope import set_FME_level
from sound_base.FM.sound_FM_envelope import set_FME_poly
from sound_base.FM.sound_FM_envelope import set_FME
from sound_base.FM.sound_FM_envelope import set_Envelope

from sound_base.FM.sound_FM_unit import SINNote
from sound_base.FM.sound_FM_unit import SINFreq
from sound_base.FM.sound_FM_unit import Freq
from sound_base.FM.sound_FM_unit import Mix
from sound_base.FM.sound_FM_unit import Modulate
from sound_base.FM.sound_FM_unit import SETEnv

#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    s0 = sin_out      (sound_a,duration,note-48 ,1.0,sampling)

    s1 = pulse_out    (sound_a,duration,note + 11.99,0.5,1.0,sampling)

    s2 = pulse_out     (sound_a,duration,note       ,0.5,1.0,sampling)


    s1a = fourier_trans_ratio(s1,Freq(sound_a,note + 11.99),4,20,sampling)

    s2a = fourier_trans_ratio(s2,Freq(sound_a,note        ),4,20,sampling)

    sa = Mix(s1a,s2a,0.3)

    cutoff = Freq(sound_a,note) * 3.0

    level = 0.7

    resonance = 3.0

    amount = Freq(sound_a,note) * 1.0

    env = amount * s0

    sb = EGFilter(sampling,sa,cutoff,level,resonance,env)

    set_FME_level(100, 80, 60,  0)
    set_FME_poly ( 88, 85, 60, 10)

    so = set_FME(sb,duration)

    return limitter(so)

#
# MAKING ENDS
#

