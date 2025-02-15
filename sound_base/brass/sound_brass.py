import numpy as np

from aoki.biquad_filter import LPF
from aoki.biquad_filter import BPF
from aoki.biquad_filter import filter

from sound_base.color.sound_color import sin_freq_out
from sound_base.color.sound_color import sin_jitter
from sound_base.effect.sound_effector import limitter

from sound_base.touch.sound_touch_ADSR import set_touch_ADSR
from sound_base.touch.sound_touch_ADSR import touch_ADSR

def tone_mix_flute(tone,part) :

    mix = np.zeros(part)

    mix[ 0] = 0.932
    mix[ 1] = 0.042
    mix[ 2] = 0.175
    mix[ 3] = 0.014
    mix[ 4] = 0.029
    mix[ 5] = 0.008
    mix[ 6] = 0.026
    mix[ 7] = 0.015
    mix[ 8] = 0.019
    mix[ 9] = 0.010
    mix[10] = 0.010
    mix[11] = 0.008
    mix[12] = 0.004
    mix[13] = 0.003
    mix[14] = 0.001
    mix[15] = 0.001
    mix[16] = 0.001
    mix[17] = 0.001
    mix[18] = 0.001
    mix[19] = 0.001
    mix[20] = 0.001
    mix[21] = 0.001
    mix[22] = 0.000
    mix[23] = 0.001
    mix[24] = 0.000
    mix[25] = 0.001
    mix[26] = 0.000
    mix[27] = 0.001
    mix[28] = 0.000
    mix[29] = 0.001

    return mix
    
def tone_mix_trumpet(tone,part) :

    mix = np.zeros(10)

    mix[ 0] = 0.100
    mix[ 1] = 0.200
    mix[ 2] = 0.300
    mix[ 3] = 0.400
    mix[ 4] = 0.800
    mix[ 5] = 0.400
    mix[ 6] = 0.300
    mix[ 7] = 0.200
    mix[ 8] = 0.100
    mix[ 9] = 0.050

    return mix
  
def tone_val01(freq,p1,p2,p3,p4) :

    val  = 1 / ( 1 + np.exp( - ( freq - p1 ) / p3 ) ) * p4 + p2

    return val
    
def tone_val02(freq,p1,p2,p3,p4) :

    val  = ( 1 -  1 / ( 1 + np.exp( - ( freq - p1 ) / p3 ) ) ) * p4 + p2

    return val
    
def tone_control01(freq,part,p1,p2,p3,p4) :

    ctr = np.zeros(part)

    for i in range(part) :

        ctr[i] = tone_val01(freq * (i+1),p1,p2,p3,p4)

    return ctr
    
def tone_control02(freq,part,p1,p2,p3,p4) :

    ctr = np.zeros(part)

    for i in range(part) :

        ctr[i] = tone_val02(freq * (i+1),p1,p2,p3,p4)

    return ctr
    
def tone_flat(val,part) :

    ctr = np.repeat(val,part)

    return ctr

def tone_jitter(sampling,fj,tone,duration) :

    w = np.zeros(duration)

    for n in range(duration) :

        w[n] = np.random.rand() * 2 -1

    Q = 1 / np.sqrt(2)

    a,b = LPF(sampling,fj,Q)

    jitter = filter(a,b,w)

    jitter /= np.max(np.abs(jitter))

    jitter_depth = tone_val01(tone,108,1,150/12,20)

    for n in range(duration) :

        jitter[n] *= jitter_depth

    return jitter

def tone_shimmer(sampling,fj,n,duration) :

    w = np.zeros(duration)

    for n in range(duration) :

        w[n] = np.random.rand() * 2 -1

    Q = 1 / np.sqrt(2)

    a,b = LPF(sampling,fj,Q)

    shimmer = filter(a,b,w)

    shimmer /= np.max(np.abs(shimmer))

    shimmer_depth = tone_val01(n,1,-0.3,10/12,0.8)

    for n in range(duration) :

        shimmer[n] *= shimmer_depth

    return shimmer




def tone_brass_flute(note,sound_a,sampling,duration) :

    freq = sound_a * np.power(2, note / 12)

    part = 30

    np.random.seed(0)

    s_master = np.zeros(duration)

    s_delay = tone_control01(freq,part,0,-0.1,8000/12,0.2)

    for n in range(1,part) :

        s_delay[n] -= s_delay[0]

    s_delay[0] = 0

    s_attack = tone_control02(freq,part,0,0.0,8000/12,0.2)

    s_decay = tone_flat(0.2,part)

    s_sustain = tone_flat(1.0,part)

    s_release = tone_control02(freq,part,0,0.2,8000/12,0.4)

    s_depth = tone_flat(1.30,part)

    s_mix = tone_mix_flute(0,part)

    for n in range(1,part) :

        s_jitter = tone_jitter(sampling,40,note,duration )

        s_shimmer = tone_shimmer(sampling,40,n,duration )

        s = sin_jitter(freq * n,s_jitter,duration,sampling)

        for i in range(duration) :

            s[i] *= s_mix[n-1]

        set_touch_ADSR(s_delay[n],s_attack[n],s_decay[n],s_sustain[n],s_release[n],s_depth[n])

        s = touch_ADSR(s)

        sh = 0

        for i in range(duration) :

            sh = 1 + s_shimmer[i]

            if (sh>=0) : s_master[i] += s[i] * sh

    return limitter(s_master)



def tone_brass_trumpet(note,sound_a,sampling,duration) :

    freq = sound_a * np.power(2, note / 12)

    part = int(6000 / freq)

    if part < 5 : part = 5
    elif part > 10 : part = 10

    np.random.seed(0)

    s_master = np.zeros(duration)

    s_delay     = tone_flat(0.15,part)
    s_attack    = tone_flat(0.00,part)
    s_sustain   = tone_flat(0.00,part)
    s_release   = tone_flat(0.15,part)
    s_depth     = tone_flat(1.30,part)

    s0_delay    = tone_flat(0.02,part)
    s0_attack   = tone_flat(0.01,part)
    s0_decay    = tone_flat(0.05,part)
    s0_sustain  = tone_flat(0.30,part)
    s0_release  = tone_flat(0.02,part)
    s0_depth    = tone_flat(3.00,part)

    s1_delay    = tone_flat(0.00,part)
    s1_attack   = tone_flat(0.00,part)
    s1_decay    = tone_flat(0.03,part)
    s1_sustain  = tone_flat(0.00,part)
    s1_release  = tone_flat(0.00,part)
    s1_depth    = tone_flat(1.30,part)


    for i in range(part) :

        f = freq * ( i + 1 ) * ( 1.00 - 0.15 )

        s1_delay[i] = tone_val01(f,3000,0,3000/12,0.03)

    for i in range(1,part) :

        s1_delay[i] = s1_delay[i] = s1_delay[0]

    s1_delay[0] = 0

    for i in range(part) :

        f = freq * ( i + 1 )

        s1_attack[i] = tone_val02(f,3000,0,3000/12,0.03)

    s1_sustain = tone_flat(1.00,part)

    for i in range(part) :

        f = freq * ( i + 1 )

        s1_release[i] = tone_val02(f,3000,0.2,3000/12,0.1)

    s_mix = tone_mix_trumpet(0,part)

    sa = np.zeros(duration)

    sb = np.zeros(duration)

    for n in range(part) :

        s_jitter = tone_jitter(sampling,20,note,duration )

        s_shimmer = tone_shimmer(sampling,40,n,duration )

        s0 = sin_freq_out(sound_a,duration,freq *( n + 1 ),1.0,sampling)

        s1 = sin_jitter(freq * ( n + 1 ),s_jitter,duration,sampling)

        for i in range(duration) :

            s0[i] = s0[i] * s_mix[n]

        for i in range(duration) :

            sh = 1 + s_shimmer[i]

            if (sh>=0) : s1[i] = s1[i] * sh * s_mix[n]

        set_touch_ADSR(s0_delay[n],s0_attack[n],s0_decay[n],s0_sustain[n],s0_release[n],s0_depth[n])

        s0 = touch_ADSR(s0)

        set_touch_ADSR(s1_delay[n],s1_attack[n],s1_decay[n],s1_sustain[n],s1_release[n],s1_depth[n])

        s1 = touch_ADSR(s1)

        sa += s0

        sb += s1

    s0 = sa * 0.3 + sb * 0.7

    f = 1500
    Q = 1 / np.sqrt(2)
    a,b = BPF(sampling,f,Q)
    s1 = filter(a,b,s0)

    f = 3000
    Q = 1 / np.sqrt(2)
    a,b = BPF(sampling,f,Q)
    s2 = filter(a,b,s1)

    s3 = limitter(s2)

    return s3

