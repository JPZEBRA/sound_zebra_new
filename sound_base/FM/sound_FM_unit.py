import numpy as np

from sound_base.FM.sound_FM_envelope import set_FME

# UNIT-TONE
def FM_unitT(sound_a,duration,note,ratio,feedback,sampling):

    length_of_s = int(duration)
    s = np.zeros(length_of_s)

    f0 = sound_a * np.power(2, note / 12)
    fm = f0*ratio

    sb = 0

    for n in range(length_of_s):
        s[n] = fm / sampling * n + sb * feedback
        sb = np.sin(2 * np.pi * s[n])

    return s

# UNIT-FREQ
def FM_unitF(sound_a,duration,f,ratio,feedback,sampling):

    length_of_s = int(duration)
    s = np.zeros(length_of_s)

    f0 = f
    fm = f0*ratio

    sb = 0

    for n in range(length_of_s):
        s[n] = fm / sampling * n + sb * feedback
        sb = np.sin(2 * np.pi * s[n])

    return s


# UNIT-SOUND
def FM_sound(sp):

    length_of_s = len(sp)
    s = np.zeros(length_of_s)

    for n in range(length_of_s):
        s[n] = np.sin(2 * np.pi * sp[n])

    so = set_FME(s)

    return so

# MIX
def FM_MIX(s1,s2,ratio):

    length_of_s = len(s1)
    s = np.zeros(length_of_s)

    for n in range(length_of_s):
         s[n] = np.sin(2 * np.pi * s1[n])*ratio + np.sin(2 * np.pi * s2[n])*(1.0 - ratio)
    return s

# MIX
def FM_ADD(s1,s2,ratio):

    length_of_s = len(s1)
    s = np.zeros(length_of_s)

    for n in range(length_of_s):
         s[n] = s1[n]*ratio + s2[n]*(1.0 - ratio)
    return s

# MODULATE
def FM_MODULATE(s1,md,power,feedback):

    width = len(s1)

    length_of_s = len(md)
    s = np.zeros(length_of_s)

    fb = 0

    idx = 0

    for n in range(length_of_s):
         s[n] = fb*feedback
         i1 = int(idx)
         i2 = i1 + 1
         f2 = idx - i1
         if 0<= i1 and i1<width :
             s[n] = s[n] + s1[i1]*(1.0-f2)
         if 0<= i2 and i2<width :
             s[n] = s[n] + s1[i2]*f2

         sb = np.sin(2 * np.pi * s[n] )

         st = md[n]
         idx = idx + (1 + st)*power
 
    return s

# MODULATE
def FM_MODULATE_S(s1,s2,power,feedback):

    width = len(s1)

    length_of_s = len(s2)
    s = np.zeros(length_of_s)

    fb = 0

    idx = 0

    for n in range(length_of_s):
         s[n] = fb*feedback
         i1 = int(idx)
         i2 = i1 + 1
         f2 = idx - i1
         if 0<= i1 and i1<width :
             s[n] = s[n] + s1[i1]*(1.0-f2)
         if 0<= i2 and i2<width :
             s[n] = s[n] + s1[i2]*f2

         sb = np.sin(2 * np.pi * s[n] )

         st = np.sin(2 * np.pi * s2[n])
         idx = idx + (1 + st)*power
 
    return s

