# E-PIANO-03

import numpy as np

#
# SOUNDS LIB
#


from sound_base.color.sound_color import sin_out
from sound_base.color.sound_color import sin_freq_out
from sound_base.color.sound_color import sawtooth_out
from sound_base.color.sound_color import sawtooth_freq_out
from sound_base.effect.sound_effector import reverse
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

    s1 = sin_out(sound_a,duration,note,1.0,sampling)
    s2 = reverse(sawtooth_out(sound_a,duration,note+1,1.0,sampling))
    s3 = reverse(sawtooth_out(sound_a,duration,note+2,1.0,sampling))

    m1 = ModulateR(s1,s2,0.6,0.0,Freq(sound_a,note),sampling)
    m2 = ModulateR(m1,s3,0.6,0.0,Freq(sound_a,note),sampling)

    sa = LPFilter(sampling,m2,Freq(sound_a,note)*8.0,0.1,2.0)

    set_FME_level(100,50,20,0)
    set_FME_poly(0,85,50,30)

    sb = SETEnv(sa,duration)

    return sb

#
# MAKING ENDS
#
