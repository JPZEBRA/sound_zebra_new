import numpy as np
from wave_file import wave_write_16bit_mono
from sound_color import sin_out
from sound_color import sin_decay

sampling = 44100

sound_a = 440

octave = 0

duration = 100000

for i in range(0,13):

    note = ( octave + 1 ) * 12 - 3 + ( i - 8)

    decay = 10
  
    s1 = sin_decay(sound_a,duration,note,0.8,sampling,decay)
    length_of_s = len(s1)
  
    s2 = sin_decay(sound_a,duration,note+4,0.4,sampling,decay)

    s3 = sin_decay(sound_a,duration,note+7,0.2,sampling,decay)

    length_of_s_master = int(duration)
    s_master = np.zeros(length_of_s_master)

    for n in range(length_of_s):
        if n>= duration : break
        s_master[n] += s1[n]
        s_master[n] += s2[n]
        s_master[n] += s3[n]

    wave_write_16bit_mono(sampling, s_master.copy(), 'snd' + str(i+1) + '.wav')
