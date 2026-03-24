# FM Cornet Ver 1.2

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
from sound_base.FM.sound_FM_pre import FM_pre_oboe
from sound_base.FM.sound_FM_pre import FM_pre_trumpetA
from sound_base.FM.sound_FM_pre import FM_pre_trumpetB
from sound_base.FM.sound_FM_pre import FM_pre_cornetA
from sound_base.FM.sound_FM_pre import FM_pre_cornetB

#
# SOUND SETTING
#


#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    FM_pre_cornetA()
    sa = FM_pre_sound(note,sound_a,sampling,duration)

    FM_pre_cornetB()
    sb = FM_pre_sound(note,sound_a,sampling,duration)

    sc1 =  white_noise(duration);
    FM_pre_suzu()
    sc2 = FM_pre_sound(note,sound_a,sampling,duration)
    FM_pre_saw()
    sc3 = FM_pre_sound(note,sound_a,sampling,duration)

    sc = ( 0.15 * sc1 +
           0.10 * sc2 +
           0.05 * sc3
          )

    for i in range(int(0.02*sampling)):
        sa[i] += sc[i] * 0.5

    cutoff    = 12000
    level     = 0.3
    resonance = 1.0
    sa = LPFilter(sampling,sa,cutoff,level,resonance)

    trem = int(sampling * 0.05)
    mute = int(sampling * 1.00)

    for i in range(trem):
        t = i / trem
        sb[i] = sa[i] * (1 - t) + sb[i] * t

    for i in range(duration - mute, duration) :
        sb[i] *=  ( ( mute - (i - (duration - mute))) / mute )

    set_FME_level(75, 88, 82,  0)
    set_FME_poly (72, 25, 30, 30)

    so = SETEnv(sb, duration)

    return limitter(so)

#
# MAKING ENDS
#

