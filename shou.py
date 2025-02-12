#
# MAIN OF SOUNDS MAKING
#

#
# SELECT SOUND COLOR
#

# SHO-01
from sound_settings.setting_sho01 import set_sound
name = "./output/sho01/sho"

#
# BASE SETTINS
#

sampling = 44100

sound_a = 440

duration = 60000*3

#
# EXTERNAL LIBRALIES
#

from aoki.wave_file import wave_write_16bit_mono

import numpy as np

# INDEX

def str02(n) :

    s = str(n)

    if(n<10) : s = "0" + s

    return s

#
# MAIN LOOP
#

for tone in range(1,12) :

    print("MAKING SOUND : " + name + str02(tone) + ".wav\n")

    sound_master = set_sound(tone,sound_a,sampling,duration)

    wave_write_16bit_mono(sampling, sound_master.copy(), name + str02(tone) + '.wav')

print("FINISH\n\n")

#
# TASK ENDS
#



