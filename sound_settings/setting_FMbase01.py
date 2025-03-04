# FM BRASS ( TEST010a )

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
from sound_base.effect.sound_effector import reverse
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

    s1 = sawtooth_out(sound_a,duration,note,1.0,sampling)

    s2 = sin_out(sound_a,duration,note,1.0,sampling)

    set_FME_level(100, 70,  0,  0)
    set_FME_poly (  0, 85, 80,  0)

    e1 = set_Envelope(duration,1.0)

    sa = e1 * s2

    sb = Modulate(s1,sa,0.1,0.0)

    cutoff = Freq(sound_a,note) * 3.0

    level = 0.1

    resonance = 0.0

    sc = LPFilter(sampling,sb,cutoff,level,resonance)

    set_FME_level(100, 80, 60,  0)
    set_FME_poly ( 88, 85, 20, 40)

    so = set_FME(sc,duration)

    return limitter(so)

#
# MAKING ENDS
#

