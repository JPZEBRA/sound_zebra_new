# FM SOUND

import numpy as np

#
# SOUNDS LIB
#


from sound_base.color.sound_color import sawtooth_out
from sound_base.effect.sound_effector import reverse

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

    s1 = SINNote(sound_a,duration,note,1.0,0.0,sampling)
    s2 = SINNote(sound_a,duration,note+5,1.0,0.0,sampling)

    s3 = sawtooth_out(sound_a,duration,note,1.0,sampling)
    s4 = sawtooth_out(sound_a,duration,note+1,1.0,sampling)
    s5 = sawtooth_out(sound_a,duration,note+2,1.0,sampling)

    s6 = ModulateR(s3,s4,0.5,0.0,Freq(sound_a,note),sampling)

    s7 = ModulateR(s6,s5,0.5,0.0,Freq(sound_a,note),sampling)

    set_FME_level(100,50,20,0)
    set_FME_poly(0,70,50,5)
    sa = SETEnv(reverse(s7),duration)

    return sa

#
# MAKING ENDS
#
