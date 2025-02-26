import numpy as np
from aoki.biquad_filter import LPF
from aoki.biquad_filter import filter

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
        a = s0[n]
        b = 0
        if ( n < length_of_si - 1 ) : b = s0[n+1]
        for r in range(ratio) :
            s1[(n-1)*ratio + r] = a + (b - a) * r / ratio;
  
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
        sum = 0
        for r in range(ratio) :
            sum += s4[n*ratio + r];
        so[n] = sum / ratio;

# level control

    so /= np.max(np.abs(so))
    so *= level

    return so
