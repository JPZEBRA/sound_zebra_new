# E-PIANO

import numpy as np

#
# SOUNDS LIB
#


from sound_base.color.sound_color import sin_out
from sound_base.color.sound_color import sin_freq_out
from sound_base.color.sound_color import sawtooth_out
from sound_base.color.sound_color import sawtooth_freq_out

from sound_base.touch.sound_touch_ADSR import set_touch_ADSR
from sound_base.touch.sound_touch_ADSR import touch_ADSR

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
from sound_base.FM.sound_FM_unit import SETEnv

#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    fx = np.array([1.00, 2.00, 4.00, 6.00, 8.00,10.00,12.00])
    pw = np.array([   9,    7,    5,    4,    3,    2,    1])
    fb = np.array([0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00])

    pt = np.sum(pw)
    pw = pw/pt
   
    s11  = SINNote(sound_a,duration,note,fx[0],fb[0],sampling)
    s12  = SINNote(sound_a,duration,note,fx[1],fb[1],sampling)
    s13  = SINNote(sound_a,duration,note,fx[2],fb[2],sampling)
    s14  = SINNote(sound_a,duration,note,fx[3],fb[3],sampling)
    s15  = SINNote(sound_a,duration,note,fx[4],fb[4],sampling)
    s16  = SINNote(sound_a,duration,note,fx[5],fb[5],sampling)
    s17  = SINNote(sound_a,duration,note,fx[6],fb[6],sampling)

    set_touch_ADSR(0.0000,0.00,0.05,0.30,0.30,1.30)
    t11  = touch_ADSR(s11)

    set_touch_ADSR(0.0001,0.10,0.50,0.20,0.35,1.30)
    t12  = touch_ADSR(s12)

    set_touch_ADSR(0.0002,0.09,0.55,0.15,0.40,1.30)
    t13  = touch_ADSR(s13)

    set_touch_ADSR(0.0003,0.08,0.60,0.10,0.45,1.30)
    t14  = touch_ADSR(s14)

    set_touch_ADSR(0.0004,0.07,0.65,0.07,0.50,1.30)
    t15  = touch_ADSR(s15)

    set_touch_ADSR(0.0005,0.06,0.70,0.05,0.55,1.30)
    t16  = touch_ADSR(s16)

    set_touch_ADSR(0.0006,0.05,0.75,0.03,0.60,1.30)
    t17  = touch_ADSR(s17)
 
    s1   = pw[0]*t11 + pw[1]*t12 + pw[2]*t13 + pw[3]*t14 + pw[4]*t15 + pw[5]*t16 + pw[6]*t17

    return limitter(s1)

#
# MAKING ENDS
#
