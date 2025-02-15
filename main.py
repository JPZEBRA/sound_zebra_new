import numpy as np

# WAVE SUPPORT #
from aoki.wave_file import wave_write_16bit_mono

# SOUND EFFECTORS #
from aoki.sound_effects import reverb
from aoki.sound_effects import compressor
from sound_base.effect.sound_effector import radio
from sound_base.effect.sound_effector import acoustic

#
# MAIN OF SOUNDS MAKING
#


#
# TEST MODE
#

test = False

octave = 5

key = 5

#
# BASE SETTINS
#

sampling = 44100

sound_a = 440

base_key = 69

duration = 120000


#
# SELECT SOUND COLOR
#


# SIN-01
#from sound_settings.setting_sin01 import set_sound
#name = "./output/sin01/sin"

# SQUARE-01
#from sound_settings.setting_square01 import set_sound
#name = "./output/sqr01/sqr"

# PULSE-01
from sound_settings.setting_pulse01 import set_sound
name = "./output/pls01/pls"

# SAWTOOTH-01
#from sound_settings.setting_square01 import set_sound
#name = "./output/saw01/saw"

# E-PIANO-01
#from sound_settings.setting_epiano import set_sound
#name = "./output/ep01/ep"

# E-PIANO-02
#from sound_settings.setting_FM01 import set_sound
#name = "./output/ep02/fp"

# E-PIANO-03
#from sound_settings.setting_FM02 import set_sound
#name = "./output/ep03/en"

# STRING-01
#from sound_settings.setting_string01 import set_sound
#name = "./output/str01/str"

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

# GLOCKEN-01
#from sound_settings.setting_glocken01 import set_sound
#name = "./output/glo01/glo"

# MARIMBA-01
#from sound_settings.setting_marimba01 import set_sound
#name = "./output/mar01/mar"

# FLUTE-01
#from sound_settings.setting_flute01 import set_sound
#name = "./output/flu01/flu"

# TRUMPET-01
from sound_settings.setting_trumpet01 import set_sound
name = "./output/tru01/tru"

# HARPSICHORD-01
#from sound_settings.setting_harp01 import set_sound
#name = "./output/hrp01/hrp"
#base_key = 0

# TEST
#from sound_settings.setting_FM00 import set_sound
#name = "./output/tst00/tst"


#
# MAIN LOOP
#

for note in range(41,89) :

    if(test) : note = ( octave + 1 ) * 12 - 3 + ( key - 8 )

    if(test) : print("\nTEST MODE : \n\n")

    print("MAKING SOUND : " + name + str(note) + ".wav\n")

    sound_master = set_sound(note - base_key,sound_a,sampling,duration)

    wave_write_16bit_mono(sampling, sound_master.copy(), name + str(note) + '.wav')

    if(test) : break


print("FINISH\n\n")

#
# TASK ENDS
#



