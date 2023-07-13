# FM SOUND #1 FM Electric Piano

import numpy as np

from aoki.wave_file import wave_write_16bit_mono

from sound_FM_envelope import set_FME_level
from sound_FM_envelope import set_FME_poly

from sound_FM_unit import FM_unitT
from sound_FM_unit import FM_MODULATE
from sound_FM_unit import FM_ADD
from sound_FM_unit import FM_MIX
from sound_FM_unit import FM_sound

sampling = 44100

sound_a = 440

octave = -1

duration = 60000

for tone in range(41,89) :

#    note = ( octave + 1 ) * 12 - 3 + ( i - 8)

    note = tone - 69

    ratio1 = 1.000
    ratio2 = 2.000
    feedback1 = 0.1

    set_FME_level(100,60,10,0)
    set_FME_poly(0,60,30,5)
    op6 = FM_unitT(sound_a,duration,note,ratio1,feedback1,sampling)
    s6 = FM_sound(op6)

    set_FME_level(100,60,10,0)
    set_FME_poly(0,60,30,5)
    op4 = FM_unitT(sound_a,duration,note,ratio1,0.0,sampling)
    sc = FM_sound(op4)
    m4 = FM_MODULATE(op4,s6,1.0,0.0)
    s4 = FM_sound(m4)

    set_FME_level(100,60,10,0)
    set_FME_poly(0,60,30,5)
    op5 = FM_unitT(sound_a,duration,note,ratio2,0.0,sampling)
    m5 = FM_MODULATE(op5,s6,1.0,0.0)
    s5 = FM_sound(m5)

    mix = 0.7

    sa = FM_ADD(s4,s5,mix)

    ratio3 = 1.000
    ratio4 = 7.000
    ratio5 = 17.000

    set_FME_level(100,60,5,0)
    set_FME_poly(0,80,60,5)
    op3 = FM_unitT(sound_a,duration,note,ratio5,0.0,sampling)
    s3 = FM_sound(op3)

    set_FME_level(100,60,5,0)
    set_FME_poly(0,80,60,5)
    op2 = FM_unitT(sound_a,duration,note,ratio4,0.0,sampling)
    m2 = FM_MODULATE(op2,s3,1.0,0.0)
    s2 = FM_sound(m2)

    set_FME_level(100,60,5,0)
    set_FME_poly(0,80,60,5)
    op1 = FM_unitT(sound_a,duration,note,ratio3,0.0,sampling)
    m1 = FM_MODULATE(op1,s2,1.0,0.0)
    sb = FM_sound(op1)

    mix = 0.7

    s_master = FM_ADD(sa,sb,0.7)

 
    if tone > 72 : s_master = sc

    wave_write_16bit_mono(sampling, s_master.copy(), './fm/fp' + str(tone) + '.wav')

