# FM STRING ( TEST011 )

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

    lfo = 0.2

    detune = 0.1

    s0 = tri_out(sound_a,duration,note-96,lfo,sampling)

    s1 = pulse_out_mod(sound_a,duration,note,s0,1.0,sampling)

    s2 = sawtooth_out(sound_a,duration,note + detune,1.0,sampling)

    sa = fourier_trans_ratio_sync(s1,Freq(sound_a,note),4,20,sampling)

    sb = Mix(sa,s2,0.5)

    cutoff = Freq(sound_a,note) * 3.0

    level = 0.5

    resonance = 0.0

    sc = LPFilter(sampling,sb,cutoff,level,resonance)

    set_FME_level(100, 80, 60,  0)
    set_FME_poly (  0, 85, 60, 10)

    so = SETEnv(sc,duration)

    return limitter(so)

#
# MAKING ENDS
#

