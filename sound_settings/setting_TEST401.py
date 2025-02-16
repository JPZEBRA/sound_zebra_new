# E-PIANO

import numpy as np

#
# SOUNDS LIB
#


from sound_base.color.sound_color import sin_out
from sound_base.color.sound_color import sin_freq_out
from sound_base.color.sound_color import pulse_out
from sound_base.color.sound_color import sawtooth_out
from sound_base.color.sound_color import sawtooth_freq_out

from sound_base.effect.sound_effector import limitter
from sound_base.effect.sound_effector import reverse
from sound_base.effect.sound_effector import LPFilter
from sound_base.effect.sound_effector import HPFilter

from sound_base.FM.sound_FM_envelope import set_FME_level
from sound_base.FM.sound_FM_envelope import set_FME_poly

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

    fx = np.array([1.00, 2.00, 4.00, 6.00, 8.00])
    pw = np.array([   5,    7,    9,    2,    1])
    fb = np.array([0.02, 0.01, 0.00, 0.00, 0.00])

    pt = np.sum(pw)
    pw = pw/pt
   
    s11  = SINNote(sound_a,duration,note,fx[0],fb[0],sampling)
    s12  = SINNote(sound_a,duration,note,fx[1],fb[1],sampling)
    s13  = SINNote(sound_a,duration,note,fx[2],fb[2],sampling)
    s14  = SINNote(sound_a,duration,note,fx[3],fb[3],sampling)
    s15  = SINNote(sound_a,duration,note,fx[4],fb[4],sampling)
 
    s1   = pw[0]*s11 + pw[1]*s12 + pw[2]*s13 + pw[3]*s14 + pw[4]*s15

    s2  = SINNote(sound_a,duration,note+1,1.0,0.0,sampling)

    s3  = sawtooth_out(sound_a,duration,note-3,1.0,sampling)
    s4  = sawtooth_out(sound_a,duration,note-4,1.0,sampling)
    s5  = sawtooth_out(sound_a,duration,note-7,1.0,sampling)

    m1 = Modulate(s1,s2,0.6,0.0)
    m2 = Sync(s3,s4)
    m3 = Sync(m2,s5)
    m4 = Modulate(m1,m3,0.5,0.0)

    set_FME_level(100,70,20,0)
    set_FME_poly(0,70,50,20)

    so = SETEnv(m4,duration)

    return limitter(so)

#
# MAKING ENDS
#
