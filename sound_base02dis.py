import numpy as np
from wave_file import wave_write_16bit_mono
from sound_color import sound_string
from distortion import distortion

sampling = 44100

sound_a = 440

octave = -1

duration = 100000

for i in range(0,13):

    note = ( octave + 1 ) * 12 - 3 + ( i - 8)

    s0 = sound_string(sound_a,duration,note,sampling)

    s1 = sound_string(sound_a,duration,note-13*2,sampling)

    s2 = sound_string(sound_a,duration,note-13*3,sampling)

    length_of_s_master = int(duration)

    s_master = np.zeros(length_of_s_master)

    for n in range(length_of_s_master) :
        s_master[n] += 0.5*s0[n]
        s_master[n] += 0.5*s1[n]

    gain = 1000
    level = 0.7

    s_distortion = distortion(sampling,gain,level,s_master)

    wave_write_16bit_mono(sampling, s_distortion.copy(), 'snd' + str(i+1) + 'dis.wav')
