# FM Clarinet Ver 1.2

import numpy as np

from sound_base.color.sound_color import sin_out
from sound_base.color.sound_color import pulse_out
from sound_base.color.sound_color import square_out
from sound_base.color.sound_color import pulse_out_mod
from sound_base.color.sound_color import sawtooth_out
from sound_base.color.sound_color import tri_out
from sound_base.color.sound_color import white_noise

from sound_base.effect.sound_effector import limitter
from sound_base.effect.sound_effector import LPFilter
from sound_base.effect.sound_effector import HPFilter
from sound_base.effect.sound_effector import BPFilter
from sound_base.effect.sound_effector import EGFilter

from sound_base.FM.sound_FM_envelope import set_FME_tone
from sound_base.FM.sound_FM_envelope import set_FME_organ
from sound_base.FM.sound_FM_envelope import set_FME_gentle
from sound_base.FM.sound_FM_envelope import set_FME_soft
from sound_base.FM.sound_FM_envelope import set_FME_solid
from sound_base.FM.sound_FM_envelope import set_FME_hard
from sound_base.FM.sound_FM_envelope import set_FME_very_hard
from sound_base.FM.sound_FM_envelope import set_FME_attack
from sound_base.FM.sound_FM_envelope import set_FME_slow
from sound_base.FM.sound_FM_envelope import set_FME

from sound_base.FM.sound_FM_envelope import set_FME_level
from sound_base.FM.sound_FM_envelope import set_FME_poly

from sound_base.FM.sound_FM_unit import SINNote
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
from sound_base.FM.sound_FM_pre import FM_pre_suzu
from sound_base.FM.sound_FM_pre import FM_pre_guitar
from sound_base.FM.sound_FM_pre import FM_pre_church
from sound_base.FM.sound_FM_pre import FM_pre_clarinet

#
# SOUND SETTING
#


#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    FM_pre_clarinet()

    s0 = FM_pre_sound(note,sound_a,sampling,duration)

    md = SINNote(sound_a, duration, note - 12, 1.0, 0.0, sampling)
    bre = white_noise(duration) * 0.01
    s1 = s0 + md * 0.03 + bre

    delay = np.random.uniform(-0.003, 0.003)  # -3ms〜+3ms
    s1 = np.roll(s1, int(delay * sampling))

    set_FME_soft()

    so = set_FME(s1,duration)

    return limitter(so)

#
# MAKING ENDS
#

