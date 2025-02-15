# E-PIANO-03

import numpy as np

#
# SOUNDS LIB
#


from sound_base.color.sound_color import sawtooth_out
from sound_base.effect.sound_effector import LPFilter

from sound_base.FM.sound_FM_envelope import set_FME_level
from sound_base.FM.sound_FM_envelope import set_FME_poly

from sound_base.FM.sound_FM_unit import SINNote
from sound_base.FM.sound_FM_unit import SINFreq
from sound_base.FM.sound_FM_unit import Freq
from sound_base.FM.sound_FM_unit import Mix
from sound_base.FM.sound_FM_unit import Modulate
from sound_base.FM.sound_FM_unit import ModulateR
from sound_base.FM.sound_FM_unit import SETEnv

#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    s1 = sawtooth_out(sound_a,duration,note,1.0,sampling)

    sa = LPFilter(sampling,s1,Freq(sound_a,note)*8.0,0.1,2.0)

    set_FME_level(100,50,20,0)
    set_FME_poly(0,85,50,30)

    sb = SETEnv(sa,duration)

    return sb

#
# MAKING ENDS
#
