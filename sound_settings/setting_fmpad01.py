# FM-PAD ( TEST105b )

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

    fx = np.array([ 1.00,18.90, 8.00, 0.002, 1.00, 0.002])
    fb = np.array([ 0.00, 0.00, 0.00, 0.00 , 0.00, 0.00 ])

    s11  = SINNote(sound_a,duration,note,fx[0],fb[0],sampling)
    s12  = SINNote(sound_a,duration,note,fx[1],fb[1],sampling)
    s13  = SINNote(sound_a,duration,note,fx[2],fb[2],sampling)
    s14  = SINNote(sound_a,duration,note,fx[3],fb[3],sampling)
    s15  = SINNote(sound_a,duration,note,fx[4],fb[4],sampling)
    s16  = SINNote(sound_a,duration,note,fx[5],fb[5],sampling)

    set_FME_level(100,50,30,30)
    set_FME_poly (  0,80,30, 0)

    e12 = SETEnv(s12,duration)

    m11 = Modulate(s11,e12,0.7,0.0)

    set_FME_level(100, 0, 0, 0)
    set_FME_poly (  0,45, 0, 0)

    e11 = SETEnv(m11,duration)

    set_FME_level(100, 40, 30,  0)
    set_FME_poly ( 60, 60, 20, 80)

    e14 = SETEnv(s14,duration)

    m13 = Modulate(s13,e14,0.01,0.0)

    set_FME_level(100, 95, 90,  0)
    set_FME_poly ( 85, 30, 30, 50)

    e13 = SETEnv(m13,duration)

    set_FME_level(100,100, 100,  0)
    set_FME_poly ( 85,  0,   0, 85)

    e16 = SETEnv(s16,duration)

    m15 = Modulate(s15,e16,0.02,0.3)

    set_FME_level(100, 95, 90,  0)
    set_FME_poly ( 85, 30, 30, 50)

    e15 = SETEnv(m15,duration)

    so = 0.5 * e11 + 0.1 * e13 + 0.4 * e15


    return limitter(so)

#
# MAKING ENDS
#
