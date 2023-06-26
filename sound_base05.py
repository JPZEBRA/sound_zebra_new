import numpy as np
from wave_file import wave_write_16bit_mono
from sound_color import sawtooth_out
from biquad_filter import LPF
from biquad_filter import filter


sampling = 44100

sound_a = 440

octave = 0

fcut = 1000

quality = 1/np.sqrt(2)

duration = 100000

for i in range(0,13):

    note = ( octave + 1 ) * 12 - 3 + ( i - 8)

    pow = 1.0

    s1 = sawtooth_out(sound_a,duration,note,pow*0.8,sampling)
    s2 = sawtooth_out(sound_a,duration,note+4,pow*0.4,sampling)
    s3 = sawtooth_out(sound_a,duration,note+7,pow*0.2,sampling)

    length_of_s_master = int(duration)
    s_master = np.zeros(length_of_s_master)

    for n in range(length_of_s_master):
        if n>= duration : break
        s_master[n] += s1[n]
        s_master[n] += s2[n]
        s_master[n] += s3[n]

    a,b = LPF(sampling,fcut,quality)

    s_filterd = filter(a,b,s_master)
  

    wave_write_16bit_mono(sampling, s_filterd.copy(), 'snd' + str(i+1) + 's.wav')

