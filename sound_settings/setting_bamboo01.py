 DUB BAMBOO BASS ( TEST010C )

import numpy as np

# SOUNDS LIB
from sound_base.color.sound_color import sin_out
from sound_base.color.sound_color import pulse_out

from sound_base.effect.sound_effector import limitter
from sound_base.effect.sound_effector import EGFilter

from sound_base.FM.sound_FM_envelope import set_FME_level
from sound_base.FM.sound_FM_envelope import set_FME_poly
from sound_base.FM.sound_FM_envelope import set_FME

from sound_base.FM.sound_FM_unit import Mix
from sound_base.FM.sound_FM_unit import Modulate
from sound_base.FM.sound_FM_unit import Freq


# SOUND MAKING
def set_sound(note, sound_a, sampling, duration):

    # 1. 竹の胴体（奇数倍音の中空共鳴）
    body_a = sin_out(sound_a, duration, note,     1.0, sampling)
    body_b = sin_out(sound_a, duration, note + 7, 1.0, sampling)
    body = body_a * body_b

    # 2. 竹の硬さ（軽い金属感）
    hard = sin_out(sound_a, duration, note + 12, 1.0, sampling)
    bamboo_core = Modulate(body, hard, 1.2, 0.0)

    # 3. サブ（竹の低音の補強）
    sub = sin_out(sound_a, duration, note - 12, 0.2, sampling)
    sc = Mix(bamboo_core, sub, 0.2)

    # 4. フィルタ（竹の共鳴ピーク）
    cutoff = Freq(sound_a, note) * 12
    level = 0.7
    resonance = 2.0

    # 竹はアタックが速い
    env = sin_out(sound_a, duration, note + 30, 0.3, sampling)

    se = EGFilter(sampling, sc, cutoff, level, resonance, env)

    # 5. FME（竹のアタックを強調）
    set_FME_level(100, 40, 20, 0)
    set_FME_poly (95, 70, 40, 10)

    so = set_FME(se, duration)

    return limitter(so)

# MAKING ENDS
