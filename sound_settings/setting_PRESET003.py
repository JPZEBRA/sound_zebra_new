# PRESET 003

import numpy as np

from sound_base.color.sound_color import sin_out
from sound_base.color.sound_color import pulse_out
from sound_base.color.sound_color import square_out
from sound_base.color.sound_color import pulse_out_mod
from sound_base.color.sound_color import sawtooth_out
from sound_base.color.sound_color import tri_out

from sound_base.effect.sound_effector import limitter
from sound_base.effect.sound_effector import LPFilter
from sound_base.effect.sound_effector import HPFilter
from sound_base.effect.sound_effector import BPFilter
from sound_base.effect.sound_effector import EGFilter

from sound_base.FM.sound_FM_envelope import set_FME_level
from sound_base.FM.sound_FM_envelope import set_FME_poly
from sound_base.FM.sound_FM_envelope import set_FME
from sound_base.FM.sound_FM_envelope import set_Envelope

from sound_base.FM.sound_FM_unit import Freq
from sound_base.FM.sound_FM_unit import Mix
from sound_base.FM.sound_FM_unit import Modulate
from sound_base.FM.sound_FM_unit import Sync
from sound_base.FM.sound_FM_unit import SETEnv

from sound_base.FM.sound_FM_pre import FM_pre_sound
from sound_base.FM.sound_FM_pre import FM_pre_sin
from sound_base.FM.sound_FM_pre import FM_pre_square
from sound_base.FM.sound_FM_pre import FM_pre_pulse066
from sound_base.FM.sound_FM_pre import FM_pre_pulse077
from sound_base.FM.sound_FM_pre import FM_pre_saw
from sound_base.FM.sound_FM_pre import FM_pre_tri

#
# SOUND SETTING
#


#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    FM_pre_tri()

    s1 = FM_pre_sound(note,sound_a,sampling,duration)

    s2 = FM_pre_sound(note+12,sound_a,sampling,duration)

    sa = Mix(s1,s2,0.5)

    set_FME_level(100, 80, 60,  0)
    set_FME_poly ( 88, 85, 60, 10)

    so = set_FME(sa,duration)

    return limitter(so)

#
# MAKING ENDS
#


