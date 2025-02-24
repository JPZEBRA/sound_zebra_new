# '80s DETROIT ( TEST004 )

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


    s1 = pulse_out(sound_a,duration,note,0.5,1.0,sampling)
    s2 = sin_out  (sound_a,duration,note-12,1.0,sampling)

    sa = fourier_trans_ratio(s1,Freq(sound_a,note),4,20,sampling)

    sb = Mix(sa,s2,0.4)

    cutoff = Freq(sound_a,note) * 1.5

    amount = Freq(sound_a,note) * 5.0

    level = 0.5

    resonance = 0.0

    set_FME_level(100, 80, 60,  0)
    set_FME_poly (  0, 85, 70, 30)

    env = set_Envelope(duration,1.0)

    eg = amount * env

    sc = EGFilter(sampling,sb,cutoff,level,resonance,eg)

    set_FME_level(100, 80, 60,  0)
    set_FME_poly (  0, 85, 60, 10)

    so = set_FME(sc,duration)

    return limitter(so)

#
# MAKING ENDS
#
