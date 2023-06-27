import numpy as np
from wave_file import wave_write_16bit_mono
from sound_color_ADSR import set_ADSR_HARD
from sound_color_ADSR import set_ADSR_GENTRE
from sound_color_ADSR import set_ADSR_SOFT
from sound_color_ADSR import set_ADSR_IDIOT
from sound_color_ADSR import sin_out_ADSR
from sound_touch_ADSR import set_touch_HARD
from sound_touch_ADSR import set_touch_GENTRE
from sound_touch_ADSR import set_touch_SOFT
from sound_touch_ADSR import touch_ADSR

sampling = 44100

sound_a = 440

octave = -1

duration = 100000

set_ADSR_SOFT()
set_touch_GENTRE()

for i in range(0,13):

    note = ( octave + 1 ) * 12 - 3 + ( i - 8)

    decay = 10
  
    s1 = sin_out_ADSR(sound_a,duration,note,0.8,sampling)

    length_of_s = len(s1)

    s1t = touch_ADSR(s1)
  
    s2 = sin_out_ADSR(sound_a,duration,note+4,0.4,sampling)

    s2t = touch_ADSR(s2)

    s3 = sin_out_ADSR(sound_a,duration,note+7,0.2,sampling)

    s3t = touch_ADSR(s3)

    length_of_s_master = int(duration)
    s_master = np.zeros(length_of_s_master)

    for n in range(length_of_s):
        if n>= duration : break
        s_master[n] += s1t[n]
        s_master[n] += s2t[n]
        s_master[n] += s3t[n]

    s_master /= np.max(np.abs(s_master))

    wave_write_16bit_mono(sampling, s_master.copy(), 'snd' + str(i+1) + 'adsr.wav')


