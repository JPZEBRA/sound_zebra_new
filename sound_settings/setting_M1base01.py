# M1 BASE ( TEST010 )

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

    s1 = pulse_out(sound_a,duration,note,0.66,1.0,sampling)

    sa = fourier_trans_ratio(s1,Freq(sound_a,note), 4,20,sampling)

    cutoff = Freq(sound_a,note) * 3.0

    level = 0.7

    resonance = 0.2

    amount = Freq(sound_a,note) * 1.3

    set_FME_level(100, 50,  0,  0)
    set_FME_poly (  0, 88, 80,  0)

    env = set_Envelope(duration,amount)

    sb = EGFilter(sampling,sa,cutoff,level,resonance,env)

    set_FME_level(100, 80, 60,  0)
    set_FME_poly (  0, 85, 60, 10)

    so = set_FME(sb,duration)

    return limitter(so)

#
# MAKING ENDS
#

