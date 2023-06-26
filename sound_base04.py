import numpy as np
from wave_file import wave_write_16bit_mono
from sound_color import square_out
from biquad_filter import LPF
from biquad_filter import filter


sampling = 44100

sound_a = 440

octave = 0

fcut = 1200

quality = 1/np.sqrt(2)

duration = 100000

for i in range(0,13):

    note = ( octave + 1 ) * 12 - 3 + ( i - 8)

    pow = 1.0

    s0 = square_out(sound_a,duration,note,pow,sampling)

    a,b = LPF(sampling,fcut,quality)

    s1 = filter(a,b,s0)
  
    length_of_s_master = int(duration)
    s_master = np.zeros(length_of_s_master)

    for n in range(length_of_s_master):
        if n>= duration : break
        s_master[n] += s1[n]

    wave_write_16bit_mono(sampling, s_master.copy(), 'snd' + str(i+1) + 'a.wav')

