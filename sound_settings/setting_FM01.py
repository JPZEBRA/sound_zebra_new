# FM SOUND #1 FM Electric Piano

import numpy as np

#
# SOUNDS LIB
#

from sound_base.FM.sound_FM_envelope import set_FME_level
from sound_base.FM.sound_FM_envelope import set_FME_poly

from sound_base.FM.sound_FM_unit import SINNote
from sound_base.FM.sound_FM_unit import Mix
from sound_base.FM.sound_FM_unit import Modulate
from sound_base.FM.sound_FM_unit import SETEnv

#
# SOUND MAKING
#

def set_sound(note,sound_a,sampling,duration) :

    ratio1 = 1.000
    ratio2 = 2.000
    feedback1 = 0.1
    feedback2 = 0.0
    modpower2 = 1.0

    if(note>70) : modpower2 = 0.5
    if(note>80) : modpower2 = 0.1

    op6 = SINNote(sound_a,duration,note,ratio1,feedback1,sampling)

    op4 = SINNote(sound_a,duration,note,ratio1,0.0,sampling)

    md4  = Modulate(op4,op6,modpower2,feedback2)

    op5 = SINNote(sound_a,duration,note,ratio2,0.0,sampling)

    md5  = Modulate(op5,op6,modpower2,feedback2)

    mix = 0.7

    sa = Mix(md4,md5,mix)

    set_FME_level(100,50,20,0)
    set_FME_poly(0,70,50,20)
    sa = SETEnv(sa,duration)

    ratio3 = 1.000
    ratio4 = 7.000
    ratio5 = 17.000

    op3 = SINNote(sound_a,duration,note,ratio5,0.0,sampling)

    op2 = SINNote(sound_a,duration,note,ratio4,0.0,sampling)

    md2  = Modulate(op2,op3,modpower2,feedback2)

    op1 = SINNote(sound_a,duration,note,ratio3,0.0,sampling)

    sb  = Modulate(op1,md2,modpower2,feedback2)

    set_FME_level(100,60,5,0)
    set_FME_poly(0,80,60,20)
    sb = SETEnv(sb,duration)


    mix = 0.8

    sound_master = Mix(sa,sb,mix)

    return sound_master

#
# MAKING ENDS
#
