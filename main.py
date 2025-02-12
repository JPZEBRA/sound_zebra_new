#
# MAIN OF SOUNDS MAKING
#

#
# SELECT SOUND COLOR
#

# SIN-01
#from sound_settings.setting_sin01 import set_sound
#name = "./output/sin01/sin"

# SQUARE-01
#from sound_settings.setting_square01 import set_sound
#name = "./output/squ01/squ"

# E-PIANO-01
from sound_settings.setting_FM01 import set_sound
name = "./output/fp02/pp"

# BASE-01
#from sound_settings.setting_base01 import set_sound
#name = "./output/bas01/bas"

# NOISY GUITTER-01
#from sound_settings.setting_distortion01 import set_sound
#name = "./output/dis01/dis"

# CHORUS-01
#from sound_settings.setting_chorus01 import set_sound
#name = "./output/cho01/cho"

# SIREN-01
#from sound_settings.setting_siren01 import set_sound
#name = "./output/sir01/sir"

# HAWAII-01
#from sound_settings.setting_hawaii01 import set_sound
#name = "./output/hwa01/hwa"

# UFO-01
#from sound_settings.setting_UFO01 import set_sound
#name = "./output/ufo01/ufo"


#
# TEST MODE
#

test = False

octave = 5

key = 1

#
# BASE SETTINS
#

sampling = 44100

sound_a = 440

duration = 60000

#
# EXTERNAL LIBRALIES
#

from aoki.wave_file import wave_write_16bit_mono

import numpy as np


#
# MAIN LOOP
#

for tone in range(41,89) :

    note = tone - 69

    if(test) : note = ( octave + 1 ) * 12 - 3 + ( key - 8)

    note = tone - 69

    if(test) : print("\nTEST MODE : \n\n")

    print("MAKING SOUND : " + name + str(tone) + ".wav\n")

    sound_master = set_sound(note,sound_a,sampling,duration)

    wave_write_16bit_mono(sampling, sound_master.copy(), name + str(tone) + '.wav')

    if(test) : break


print("FINISH\n\n")

#
# TASK ENDS
#



