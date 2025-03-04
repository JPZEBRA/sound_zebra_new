# FUNC ( TEST005b )

import numpy as np

#
# SOUNDS LIB
#


from sound_base.color.sound_color import sin_out
from sound_base.color.sound_color import sin_freq_out
from sound_base.color.sound_color import sawtooth_out
from sound_base.color.sound_color import sawtooth_freq_out
from sound_base.color.sound_color import pulse_out
from sound_base.color.sound_color import pulse_out_mod

from sound_base.effect.sound_effector import limitter
from sound_base.effect.sound_effector import fourier_trans_ratio_sync
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

    s1 = sin_out(sound_a,duration,note-64,0.3,sampling)

    s2 = pulse_out_mod(sound_a,duration,note,s1,1.0,sampling)

    sa = fourier_trans_ratio_sync(s2,Freq(sound_a,note),4,20,sampling)

    cutoff = Freq(sound_a,note) * 2.5

    amount = Freq(sound_a,note) * 0.3

    level = 0.5

    resonance = 10.0

    set_FME_level(100, 80,  0, 0)
    set_FME_poly ( 80, 70, 60, 0)

    env = set_Envelope(duration,1.0)

    eg = amount * env

    sb = EGFilter(sampling,sa,cutoff,level,resonance,eg)

    set_FME_level(100, 80, 60,  0)
    set_FME_poly (  0, 85, 60, 10)

    so = set_FME(sb,duration)

    return limitter(so)

#
# MAKING ENDS
#
