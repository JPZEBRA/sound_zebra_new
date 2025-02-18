# E-PIANO

import numpy as np

#
# SOUNDS LIB
#


from sound_base.color.sound_color import sin_out
from sound_base.color.sound_color import sin_freq_out
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

    fx = np.array([20.00,19.52, 1.00, 1.00, 5.00])
    fb = np.array([ 0.00, 0.00, 0.00, 0.00, 0.50])

    s11  = SINNote(sound_a,duration,note,fx[0],fb[0],sampling)
    s12  = SINNote(sound_a,duration,note,fx[1],fb[1],sampling)
    s13  = SINNote(sound_a,duration,note,fx[2],fb[2],sampling)
    s14  = SINNote(sound_a,duration,note,fx[3],fb[3],sampling)
    s15  = SINNote(sound_a,duration,note,fx[4],fb[4],sampling)
    s16  = SINFreq(sound_a,duration, 100,1.00 ,0.00 ,sampling)

    set_FME_level(100,50,10,10)
    set_FME_poly (  0,70,50, 0)

    e12 = SETEnv(s12,duration)

    m11 = Modulate(s11,e12,0.7,0.0)

    set_FME_level(100,50, 0, 0)
    set_FME_poly (  0,85,50, 0)

    e11 = SETEnv(m11,duration)

    set_FME_level(100,30, 0, 0)
    set_FME_poly (  0,85,30, 0)

    e15 = SETEnv(s15,duration)

    m14 = Modulate(s14,e15,0.7,0.0)

    set_FME_level(100,60,30,30)
    set_FME_poly (  0,80,20, 0)

    e14 = SETEnv(m14,duration)

    m13 = Modulate(s13,e14,0.2,0.0)

    set_FME_level(100,50, 0, 0)
    set_FME_poly (  0,60,10, 0)

    e13 = SETEnv(m13,duration)

    set_FME_level(100,30, 0, 0)
    set_FME_poly (  0,85,80, 0)

    e16 = SETEnv(s16,duration)

    so1 = Mix(e11,e13,0.3)

    so2 = Mix(so1,e16,0.5)


    return limitter(so2)

#
# MAKING ENDS
#
