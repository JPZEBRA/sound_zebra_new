# E-PIANO ( TEST001 )

import numpy as np

from sound_base.color.sound_color import sin_out
from sound_base.color.sound_color import sin_freq_out
from sound_base.color.sound_color import sawtooth_out
from sound_base.color.sound_color import sawtooth_freq_out
from sound_base.color.sound_color import sawtooth_decay

from sound_base.effect.sound_effector import limitter
from sound_base.effect.sound_effector import reverse
from sound_base.effect.sound_effector import LPFilter
from sound_base.effect.sound_effector import HPFilter
from sound_base.effect.sound_effector import BPFilter
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

from sound_base.color.sound_color import sawtooth_decay
from aoki.biquad_filter import LPF
from aoki.biquad_filter import filter

#
# SOUND SETTING
#

decay = 1

#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    fx = np.array([1.00, 3.00, 5.00, 7.00, 9.00,11.00,13.00,0.10])
    pw = np.array([   5,    7,    9,    4,    3,    2,    1,   0])
    fb = np.array([0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,0.00])

    pt = np.sum(pw)
    pw = pw/pt
   
    s11  = SINNote(sound_a,duration,note,fx[0],fb[0],sampling)
    s12  = SINNote(sound_a,duration,note,fx[1],fb[1],sampling)
    s13  = SINNote(sound_a,duration,note,fx[2],fb[2],sampling)
    s14  = SINNote(sound_a,duration,note,fx[3],fb[3],sampling)
    s15  = SINNote(sound_a,duration,note,fx[4],fb[4],sampling)
    s16  = SINNote(sound_a,duration,note,fx[5],fb[5],sampling)
    s17  = SINNote(sound_a,duration,note,fx[6],fb[6],sampling)
    s18  = SINNote(sound_a,duration,note,fx[7],fb[7],sampling)

    s1   = pw[0]*s11 + pw[1]*s12 + pw[2]*s13 + pw[3]*s14 + pw[4]*s15 + pw[5]*s16 + pw[6]*s17

    cutoff = Freq(sound_a,note) * 1.5

    amount = Freq(sound_a,note) * 0.5

    level = 0.5

    resonance = 3.0

    env1 = amount * s18
 
    sa = EGFilter(sampling,s1,cutoff,level,resonance,env1)
 
    set_FME_level(100, 80,  0,  0)
    set_FME_poly ( 89, 89, 89,  0)

    env2 = set_Envelope(duration,1.0)

    sb = Modulate(sa,env2,-0.1,0.0)

    set_FME_level(100, 80, 30,  0)
    set_FME_poly (  0, 80, 60, 10)

    sc = set_FME(sb,duration)

    return limitter(sc)

#
# MAKING ENDS
#



