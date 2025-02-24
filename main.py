import numpy as np

# WAVE SUPPORT #
from aoki.wave_file import wave_write_16bit_mono

#
# MAIN OF SOUNDS MAKING
#


#
# TEST MODE
#

test = False

octave = 5

key = 8

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
#from sound_settings.setting_pulse01 import set_sound
#name = "./output/pls01/pls"

# SAWTOOTH-01
#from sound_settings.setting_sawtooth01 import set_sound
#name = "./output/saw01/saw"

# SAWTOOTH-02
#from sound_settings.setting_sawtooth01 import set_sound
#name = "./output/saw02/saw"

# SAWTOOTH-03
#from sound_settings.setting_sync_saw01 import set_sound
#name = "./output/saw03/saw"

# E-PIANO-01
#from sound_settings.setting_epiano01 import set_sound
#name = "./output/ep01/ep"

# E-PIANO-02
#from sound_settings.setting_FM01 import set_sound
#name = "./output/ep02/fp"

# E-PIANO-03
#from sound_settings.setting_fmpiano01 import set_sound
#name = "./output/ep03/eb"

# E-PIANO-04
#from sound_settings.setting_fmpiano02 import set_sound
#name = "./output/ep04/ex"

# E-PIANO-05
#from sound_settings.setting_fmpiano03 import set_sound
#name = "./output/ep05/ee"

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
#from sound_settings.setting_trumpet01 import set_sound
#name = "./output/tru01/tru"

# HARPSICHORD-01
#from sound_settings.setting_harp01 import set_sound
#name = "./output/hrp01/hrp"
#base_key = 0

# D-BASE-1
#from sound_settings.setting_dbase01 import set_sound
#name = "./output/dbs01/db"

# FMPAD-1
#from sound_settings.setting_fmpad01 import set_sound
#name = "./output/fmp01/fmp"

# FMPAD-2
#from sound_settings.setting_fmpad02 import set_sound
#name = "./output/fmp02/fmp"

# TECHNO-1
#from sound_settings.setting_techno01 import set_sound
#name = "./output/tec01/tec"

# TECHNO-2
#from sound_settings.setting_techno02import set_sound
#name = "./output/tec02/tec"

# DETROIT-1
#from sound_settings.setting_detroit01 import set_sound
#name = "./output/det01/det"

# FUNC-1
#from sound_settings.setting_func01 import set_sound
#name = "./output/fnc01/fnc"

# FUNC-2
#from sound_settings.setting_func02 import set_sound
#name = "./output/fnc02/fnc"

# SOLID BASE-1
#from sound_settings.setting_dbase03 import set_sound
#name = "./output/dbs03/dbs"

# DUB STEP-1
#from sound_settings.setting_dubstep01 import set_sound
#name = "./output/dub01/dub"

# DUB STEP-2 ( ISLAND )
#from sound_settings.setting_island01 import set_sound
#name = "./output/ild01/ild"

# FM STRING-1
#from sound_settings.setting_FMstring01 import set_sound
#name = "./output/fms01/fms"

# FM STRING-2
#from sound_settings.setting_FMstring02 import set_sound
#name = "./output/fms02/fms"

# FM BRASS 1
#from sound_settings.setting_FMbrass01 import set_sound
#name = "./output/fmb01/fmb"

# FM BASE-1
#from sound_settings.setting_FMbase01 import set_sound
#name = "./output/fba01/fba"

# FM PAD-4
#from sound_settings.setting_FMpad04 import set_sound
#name = "./output/fmp04/fmp"

# M1 BASE-1
#from sound_settings.setting_M1base01 import set_sound
#name = "./output/m1b01/m1b"

# GORIGORI-1
#from sound_settings.setting_gorigori01 import set_sound
#name = "./output/grb01/grb"

# ORGEL
#from sound_settings.setting_suzu01 import set_sound
#name = "./output/suzu01/suzu"

# BELL
#from sound_settings.setting_suzu02 import set_sound
#name = "./output/suzu02/suzu"

# KNOCK
#from sound_settings.setting_PRESET005 import set_sound
#name = "./output/knk01/knk"

# CHURCH BELL
#from sound_settings.setting_PRESET007 import set_sound
#name = "./output/chb00/chb"

# GUITAR
#from sound_settings.setting_PRESET008 import set_sound
#name = "./output/gtr01/gtr"

# DRUM
from sound_settings.setting_PRESET010 import set_sound
name = "./output/drm01/drm"

# VOCAL
#from sound_settings.setting_PRESET011 import set_sound
#name = "./output/voc01/voc"

# RG-HORN
#from sound_settings.setting_PRESET012 import set_sound
#name = "./output/rgh01/rgh"

# HONK
#from sound_settings.setting_PRESET013 import set_sound
#name = "./output/hnk01/hnk"

# HIPHOP
from sound_settings.setting_hiphop01 import set_sound
name = "./output/hip01/hip"

# TEST
from sound_settings.setting_PRESET000 import set_sound
name = "./output/tst000/tst"

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



