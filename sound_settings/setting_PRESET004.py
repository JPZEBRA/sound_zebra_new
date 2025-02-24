# PRESET 004

import numpy as np

from aoki.sound_effects import reverb

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

from sound_base.FM.sound_FM_envelope import set_FME_tone
from sound_base.FM.sound_FM_envelope import set_FME_organ
from sound_base.FM.sound_FM_envelope import set_FME_gentle
from sound_base.FM.sound_FM_envelope import set_FME_hard
from sound_base.FM.sound_FM_envelope import set_FME_slow
from sound_base.FM.sound_FM_envelope import set_FME

from sound_base.FM.sound_FM_envelope import set_FME_level
from sound_base.FM.sound_FM_envelope import set_FME_poly

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

    FM_pre_square()

    s1 = FM_pre_sound(note-24,sound_a,sampling,duration)
    s2 = FM_pre_sound(note   ,sound_a,sampling,duration)
    s3 = FM_pre_sound(note+12,sound_a,sampling,duration)

    s4 = Modulate(s2,s3,0.1,0.0)

    sa = 0.2 * s1 + 0.5 * s4 + 0.3 * s3

    cutoff = Freq(sound_a,note) * 3.0

    level = 0.5

    resonance = 3.0

    sb = LPFilter(sampling,sa,cutoff,level,resonance)

    set_FME_hard()

    sc = set_FME(sb,duration)

    so = reverb(sampling,2.0,0.5,sc)

    return limitter(so)

#
# MAKING ENDS
#

