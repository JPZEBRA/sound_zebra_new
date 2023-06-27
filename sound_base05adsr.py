import numpy as np
from wave_file import wave_write_16bit_mono

from sound_color_ADSR import set_ADSR_HARD
from sound_color_ADSR import set_ADSR_GENTRE
from sound_color_ADSR import set_ADSR_SOFT
from sound_color_ADSR import set_ADSR_IDIOT
from sound_color_ADSR import sawtooth_out_ADSR
from biquad_filter import LPF
from biquad_filter import filter

from sound_touch_ADSR import set_touch_HARD
from sound_touch_ADSR import set_touch_GENTRE
from sound_touch_ADSR import set_touch_SOFT
from sound_touch_ADSR import touch_ADSR


sampling = 44100

sound_a = 440

octave = 0

fcut = 1000

quality = 1/np.sqrt(2)

duration = 100000

set_ADSR_GENTRE()

set_touch_GENTRE()

for i in range(0,13):

    note = ( octave + 1 ) * 12 - 3 + ( i - 8)

    pow = 1.0

    s1 = sawtooth_out_ADSR(sound_a,duration,note,pow*0.8,sampling)
    s2 = sawtooth_out_ADSR(sound_a,duration,note+4,pow*0.4,sampling)
    s3 = sawtooth_out_ADSR(sound_a,duration,note+7,pow*0.2,sampling)

    s1t = touch_ADSR(s1)
    s2t = touch_ADSR(s2)
    s3t = touch_ADSR(s3)

    length_of_s_master = int(duration)
    s_master = np.zeros(length_of_s_master)

    for n in range(length_of_s_master):
        if n>= duration : break
        s_master[n] += s1t[n]
        s_master[n] += s2t[n]
        s_master[n] += s3t[n]

    s_master /= np.max(np.abs(s_master))

    a,b = LPF(sampling,fcut,quality)

    s_filterd = filter(a,b,s_master)
  
    wave_write_16bit_mono(sampling, s_filterd.copy(), 'snd' + str(i+1) + 'adsr.wav')

