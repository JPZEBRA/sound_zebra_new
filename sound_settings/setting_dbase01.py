# D-BASE ( TEST104 )

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

    fx = np.array([ 0.50, 1.00, 2.00, 1.00,10.00, 9.00])
    fb = np.array([ 0.00, 0.70, 0.00, 0.00, 0.00, 0.00])

    s11  = SINNote(sound_a,duration,note,fx[0],fb[0],sampling)
    s12  = SINNote(sound_a,duration,note,fx[1],fb[1],sampling)
    s13  = SINNote(sound_a,duration,note,fx[2],fb[2],sampling)
    s14  = SINNote(sound_a,duration,note,fx[3],fb[3],sampling)
    s15  = SINNote(sound_a,duration,note,fx[4],fb[4],sampling)
    s16  = SINNote(sound_a,duration,note,fx[5],fb[5],sampling)

    set_FME_level(100,50,10,10)
    set_FME_poly (  0,80,70, 0)

    e12 = SETEnv(s12,duration)

    m11 = Modulate(s11,e12,0.7,0.0)

    set_FME_level(100,60,10, 0)
    set_FME_poly (  0,80,70,20)

    e11 = SETEnv(m11,duration)

    set_FME_level(100,60,70, 0)
    set_FME_poly (  0,80,10,50)

    e14 = SETEnv(s14,duration)

    set_FME_level(100,50,10, 0)
    set_FME_poly (  0,80,40,45)

    e16 = SETEnv(s16,duration)

    m15 = Modulate(s15,e16,0.7,0.0)

    set_FME_level(100,30,20, 0)
    set_FME_poly (  0,85,10,45)

    e15 = SETEnv(m15,duration)

    m00 = Mix(e14,e15,0.5)

    m13 = Modulate(s13,m00,0.7,0.0)

    set_FME_level(100,60,10, 0)
    set_FME_poly (  0,80,70,20)

    e13 = SETEnv(m13,duration)

    so = Mix(e11,e13,0.5)

    return limitter(so)

#
# MAKING ENDS
#
