# DUB BASE ISLAND ( TEST009a )

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
from sound_base.effect.sound_effector import fourier_trans
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

    s0 = sin_out      (sound_a,duration,note - 64.3 ,1.0,sampling)

    s1 = sin_out      (sound_a,duration,note - 37.3 ,1.0,sampling)

    s2 = sin_out      (sound_a,duration,note + 12,1.0,sampling)

    s3 = pulse_out    (sound_a,duration,note,0.5,1.0,sampling)

    sa = s2 * s1

#    sb = fourier_trans_ratio(s3,Freq(sound_a,note),2,50,sampling)
    sb = s3

    sc = Mix(sb,s2,0.5)

    sd = Modulate(sc,sa,3.00,0.0)

    cutoff = Freq(sound_a,note) * 5.0

    level = 0.7

    resonance = 3.0

    amount = Freq(sound_a,note) * 0.7

    env = amount * s0

    se = EGFilter(sampling,sd,cutoff,level,resonance,env)

    set_FME_level(100, 80, 60,  0)
    set_FME_poly ( 88, 85, 60, 10)

    so = set_FME(se,duration)

    return limitter(so)

#
# MAKING ENDS
#

