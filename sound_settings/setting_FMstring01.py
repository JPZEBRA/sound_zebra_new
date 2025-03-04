# FM STRING ( TEST010 )

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

    detune = 0.1

    s1 = sawtooth_out(sound_a,duration,note + detune,1.0,sampling)

    s2 = sawtooth_out(sound_a,duration,note - detune,1.0,sampling)

    sa = Mix(s1,s2,0.5)

    cutoff = Freq(sound_a,note) * 3.0

    level = 0.5

    resonance = 0.0

    amount = Freq(sound_a,note) * 1.5

    set_FME_level(100, 50,  0,  0)
    set_FME_poly ( 89, 80, 80,  0)

    env = set_Envelope(duration,amount)

    sb = EGFilter(sampling,sa,cutoff,level,resonance,env)

    set_FME_level(100, 80, 60,  0)
    set_FME_poly ( 88, 85, 60, 10)

    so = set_FME(sb,duration)

    return limitter(so)

#
# MAKING ENDS
#

