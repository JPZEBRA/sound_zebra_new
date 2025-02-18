# FM-PAD ( TEST105 )

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

    fx = np.array([ 1.00,18.90, 1.00, 7.00, 1.00, 1.00])
    fb = np.array([ 0.00, 0.00, 0.00, 0.00, 0.00, 0.50])

    s11  = SINNote(sound_a,duration,note,fx[0],fb[0],sampling)
    s12  = SINNote(sound_a,duration,note,fx[1],fb[1],sampling)
    s13  = SINFreq(sound_a,duration,   1,fx[2],fb[2],sampling)
    s14  = SINNote(sound_a,duration,note,fx[3],fb[3],sampling)
    s15  = SINFreq(sound_a,duration,   1,fx[4],fb[4],sampling)
    s16  = SINNote(sound_a,duration,note,fx[5],fb[5],sampling)

    set_FME_level(100,50,30,30)
    set_FME_poly (  0,80,30, 0)

    e12 = SETEnv(s12,duration)

    m11 = Modulate(s11,e12,0.7,0.0)

    set_FME_level(100, 0, 0, 0)
    set_FME_poly (  0,45, 0, 0)

    e11 = SETEnv(m11,duration)

    set_FME_level(100, 70,100,  0)
    set_FME_poly ( 80, 60, 60, 80)

    e14 = SETEnv(s14,duration)

    m13 = Modulate(s13,e14,100.0,0.0)

    set_FME_level(  0,100, 60,  0)
    set_FME_poly (  0, 80, 60, 50)

    e13 = SETEnv(m13,duration)

    set_FME_level( 50,100, 100, 50)
    set_FME_poly ( 60,  0,   0, 60)

    e16 = SETEnv(s16,duration)

    m15 = Modulate(s15,e16,100.0,0.3)

    set_FME_level(  0,100, 90,  0)
    set_FME_poly (  0, 80,  5, 60)

    e15 = SETEnv(m15,duration)

    so = 0.5 * e11 + 0.1 * e13 + 0.4 * e15


    return limitter(so)

#
# MAKING ENDS
#
