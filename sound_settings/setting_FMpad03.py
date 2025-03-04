# FM-PAD ( TEST105a )

import numpy as np

#
# SOUNDS LIB
#


from sound_base.color.sound_color import sin_out
from sound_base.color.sound_color import sin_freq_out
from sound_base.color.sound_color import sawtooth_out
from sound_base.color.sound_color import pulse_out
from sound_base.color.sound_color import pulse_out_trp
from sound_base.color.sound_color import sawtooth_freq_out

from sound_base.effect.sound_effector import limitter
from sound_base.effect.sound_effector import reverse
from sound_base.effect.sound_effector import LPFilter
from sound_base.effect.sound_effector import HPFilter
from sound_base.effect.sound_effector import BPFilter
from sound_base.effect.sound_effector import EGFilter

from sound_base.FM.sound_FM_envelope import set_FME_level
from sound_base.FM.sound_FM_envelope import set_FME_poly
from sound_base.FM.sound_FM_envelope import set_Envelope

from sound_base.FM.sound_FM_unit import SINNote
from sound_base.FM.sound_FM_unit import SINFreq
from sound_base.FM.sound_FM_unit import Freq
from sound_base.FM.sound_FM_unit import Mix
from sound_base.FM.sound_FM_unit import Modulate
from sound_base.FM.sound_FM_unit import Sync
from sound_base.FM.sound_FM_unit import SETEnv

#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :


    s1  = sawtooth_out (sound_a,duration,note   ,1.0,sampling)
    s2  = sawtooth_out (sound_a,duration,note+19,1.0,sampling)
    s3  = pulse_out_trp(sound_a,duration,note-12,0.5,0.2,1.0,sampling)

    sa = 0.4 * s1 + 0.4 * s2 + 0.1 * s3

    cutoff = Freq(sound_a,note) * 5.0

    level = 0.7

    resonance = 0.0

    amount = Freq(sound_a,note) * 3.0

    set_FME_level(100, 0, 0, 0)
    set_FME_poly (  0,45, 0, 0)
    env = set_Envelope(duration,amount)

    sb = EGFilter(sampling,sa,cutoff,level,resonance,env)


    set_FME_level(100, 90, 90,100)
    set_FME_poly ( 89, 80, 0,  50)

    so = SETEnv(sb,duration)

    return limitter(so)

#
# MAKING ENDS
#
