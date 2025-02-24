import sys
import numpy as np


# WAVE SUPPORT #

from aoki.wave_file import wave_read_16bit_mono

# CHECK SPECTRUM #

from sound_base.FM.sound_FM_pre import FM_pre_spectrum

# BASE SETTINS #

sampling = 44100

sound_a = 440

freq = sound_a

########
# MAIN #
########

args = sys.argv

if len(args) >= 3 :

    print("\nSPECTRUM CHECK\n")

    freq = int(args[1])

    sfile = args[2]

    cut  = 0

    end  = 0

    sampling,sound = wave_read_16bit_mono(sfile)

    slen = len(sound)

    print(str(sampling) + " Hz / " + str(slen) + " SAMPLES" )

    if len(args) > 3 : cut = int(sampling * float(args[3]))
    if len(args) > 4 : end = int(sampling * float(args[4]))
    if end > 0 and end <= cut : exit(0)

#   1.0 sec
    duration = sampling
    if end > 0 : duration = sampling * ( end - cut )

    over = duration + cut - slen
    if over > 0 : duration -= over

    sample = np.zeros(duration)

    for n in range(duration) : sample[n] = float(sound[n + cut][0])

    FM_pre_spectrum(sample,freq,20,sampling)

else :

    print("\nUSAGE : spectrum.py freq filename [start] [end]\n\n")

print("\nEND\n\n")

#############
# TASK ENDS #
#############




