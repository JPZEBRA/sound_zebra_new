# UK newwave

import numpy as np

#
# SOUNDS LIB
#


from sound_base.color.sound_color import sin_out
from sound_base.color.sound_color import sin_freq_out
from sound_base.color.sound_color import sawtooth_out
from sound_base.color.sound_color import sawtooth_freq_out
from sound_base.color.sound_color import pulse_out
from sound_base.color.sound_color import pulse_freq_out
from sound_base.color.sound_color import pulse_out_mod
from sound_base.color.sound_color import tri_out
from sound_base.color.sound_color import tri_freq_out

from sound_base.effect.sound_effector import limitter
from sound_base.effect.sound_effector import fourier_trans_ratio_sync
from sound_base.effect.sound_effector import LPFilter
from sound_base.effect.sound_effector import EGFilter

from sound_base.FM.sound_FM_envelope import set_FME_level
from sound_base.FM.sound_FM_envelope import set_FME_poly
from sound_base.FM.sound_FM_envelope import set_FME
from sound_base.FM.sound_FM_envelope import set_Envelope
from sound_base.FM.sound_FM_envelope import set_FME_tone
from sound_base.FM.sound_FM_envelope import set_FME_decay
from sound_base.FM.sound_FM_envelope import set_FME_gentle

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


    s1 = tri_freq_out(sound_a,duration,1.4,1.0,sampling)

    s2 = pulse_out_mod(sound_a,duration,note,s1,0.2,sampling)

    s3 = sawtooth_freq_out(sound_a,duration,Freq(sound_a,note)*1.01,1.0,sampling)

    sb = Mix(s2,s3,0.7)

    cutoff = Freq(sound_a,note) * 3.5

    level = 0.5

    resonance = 10.0

    sc = LPFilter(sampling,sb,cutoff,level,resonance)

    set_FME_tone()

    so = SETEnv(sc,duration)

    return limitter(so)

#
# MAKING ENDS
#
