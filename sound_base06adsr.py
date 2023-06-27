import numpy as np
from wave_file import wave_write_16bit_mono

from sound_color_ADSR import set_ADSR_HARD
from sound_color_ADSR import set_ADSR_GENTRE
from sound_color_ADSR import set_ADSR_SOFT
from sound_color_ADSR import set_ADSR_IDIOT

from sound_color_ADSR import sawtooth_out_ADSR
from biquad_filter import LPF
from biquad_filter import filter

from sound_touch_ADSR import set_touch_GENTRE
from sound_touch_ADSR import touch_ADSR
from sound_touch_ADSR import delay



sampling = 44100

sound_a = 440

octave = 0

fcut = 1000

quality = 1/np.sqrt(2)

duration = 100000

a,b = LPF(sampling,fcut,quality)

set_ADSR_IDIOT

set_touch_GENTRE

for i in range(0,13):

    note = ( octave + 1 ) * 12 - 3 + ( i - 8)

    pow = 1.0

    length_of_s_master = int(duration)
    s_master = np.zeros(length_of_s_master)

    for dt in range(0,60) :
        st = sawtooth_out_ADSR(sound_a,duration,note + (dt % 20 - 10) /17 + np.random.rand()/3,pow,sampling)
        sk = touch_ADSR(st)
        sd = delay(sk,int(np.random.rand()*100))
        sf = filter(a,b,sd)
        s_master += sf

    s_master /= np.max(np.abs(s_master))
  

    wave_write_16bit_mono(sampling, s_master.copy(), 'snd' + str(i+1) + 'cor-adsr.wav')

