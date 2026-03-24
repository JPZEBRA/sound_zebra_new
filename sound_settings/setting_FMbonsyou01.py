# FM BONSYOU Ver 0.1

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
from sound_base.color.sound_color import tri_out
from sound_base.color.sound_color import tri_freq_out

from sound_base.effect.sound_effector import limitter
from sound_base.effect.sound_effector import fourier_trans
from sound_base.effect.sound_effector import fourier_trans_sync
from sound_base.effect.sound_effector import fourier_trans_ratio
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

    f = Freq(sound_a,note)

    s01 = SINFreq(sound_a,duration,f*0.80,1.0,0.0,sampling)
    s02 = SINFreq(sound_a,duration,f*1.00,1.0,0.0,sampling)
    s03 = SINFreq(sound_a,duration,f*2.30,1.0,0.0,sampling)
    s04 = SINFreq(sound_a,duration,f*3.05,1.0,0.0,sampling)
    s05 = SINFreq(sound_a,duration,f*4.80,1.0,0.0,sampling)


    set_FME_level( 20, 30, 40,  0)
    set_FME_poly ( 60, 10, 10, 10)
    s01 = SETEnv (s01,duration)

    set_FME_level(100, 30, 20,  0)
    set_FME_poly ( 80, 40, 10, 10)
    s02 = SETEnv (s02,duration)

    set_FME_level(100, 30, 20,  0)
    set_FME_poly ( 85, 70, 10, 10)
    s03 = SETEnv (s03,duration)

    set_FME_level(100, 30, 20,  0)
    set_FME_poly ( 83, 65, 10, 10)
    s04 = SETEnv (s04,duration)

    set_FME_level(100, 30, 20,  0)
    set_FME_poly ( 85, 80, 10, 10)
    s05 = SETEnv (s05,duration)

    so = s01 + s02 + s03 + s04 + s05

    return limitter(so)

#
# MAKING ENDS
#

