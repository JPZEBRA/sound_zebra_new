import numpy as np
from wave_file import wave_write_16bit_mono
from sound_color import FM_out

sampling = 44100

sound_a = 440

octave = -1

duration = 100000

for i in range(0,13):

    note = ( octave + 1 ) * 12 - 3 + ( i - 8)

    ratio = 1.012

    pow = 1.0

    pow_m = 1.0

    s0 = FM_out(sound_a,duration,note,pow,ratio,pow_m,sampling)
  
    length_of_s_master = int(duration)
    s_master = np.zeros(length_of_s_master)

    for n in range(length_of_s_master):
        if n>= duration : break
        s_master[n] += s0[n]

    wave_write_16bit_mono(sampling, s_master.copy(), 'snd' + str(i+1) + 'a.wav')

