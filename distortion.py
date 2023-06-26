import numpy as np
from wave_file import wave_write_16bit_mono
from biquad_filter import LPF
from biquad_filter import filter

def distortion(sampling,gain,level,si) :

    length_of_si = len(si)

    so = np.zeros(length_of_si)

# LPF 2000Hz

    fcut = 2000
    quality = 1 / np.sqrt(2)
    a,b = LPF(sampling,fcut,quality)
    s0 = filter(a,b,si)

# 4x Up-Sampling

    ratio = 4
    s1 = np.zeros(length_of_si * ratio )
    for n in range(length_of_si) :
        for r in range(ratio) :
            s1[(n-1)*ratio + r] = s0[n];
  
# LPF 20000Hz

    fcut = 20000 / ratio
    quality = 1 / np.sqrt(2)
    a,b = LPF(sampling,fcut,quality)
    s2 = filter(a,b,s1)

# DISTORTION !!!

    s3 = np.zeros(length_of_si * ratio )
    for n in range(length_of_si*ratio) :
        s3[n] = np.tanh( 5 * s2[n] * gain / 2 );
    
# LPF 20000Hz

    fcut = 20000 / ratio
    quality = 1 / np.sqrt(2)
    a,b = LPF(sampling,fcut,quality)
    s4 = filter(a,b,s3)

# 1/4 Down-Sampling

    for n in range(length_of_si) :
        so[n] = s4[(n-1)*ratio] = s0[n];

# level control

    so /= np.max(np.abs(so))
    so *= level

    return so
