# ISEKAI CHURCH

import numpy as np

from sound_base.color.sound_color import sin_out
from sound_base.color.sound_color import pulse_out
from sound_base.color.sound_color import square_out
from sound_base.color.sound_color import pulse_out_mod
from sound_base.color.sound_color import sawtooth_out
from sound_base.color.sound_color import tri_out

from sound_base.effect.sound_effector import limitter
from sound_base.effect.sound_effector import LPFilter
from sound_base.effect.sound_effector import HPFilter
from sound_base.effect.sound_effector import BPFilter
from sound_base.effect.sound_effector import EGFilter

from sound_base.FM.sound_FM_envelope import set_FME_level
from sound_base.FM.sound_FM_envelope import set_FME_poly
from sound_base.FM.sound_FM_envelope import set_FME_hard
from sound_base.FM.sound_FM_envelope import set_FME_solid
from sound_base.FM.sound_FM_envelope import set_FME
from sound_base.FM.sound_FM_envelope import set_Envelope

from sound_base.FM.sound_FM_unit import Freq
from sound_base.FM.sound_FM_unit import SINFreq
from sound_base.FM.sound_FM_unit import CNoiseFreq
from sound_base.FM.sound_FM_unit import Mix
from sound_base.FM.sound_FM_unit import Modulate
from sound_base.FM.sound_FM_unit import Sync
from sound_base.FM.sound_FM_unit import SETEnv

from sound_base.FM.sound_FM_pre import FM_pre_sound
from sound_base.FM.sound_FM_pre import FM_pre_sin
from sound_base.FM.sound_FM_pre import FM_pre_square
from sound_base.FM.sound_FM_pre import FM_pre_pulse066
from sound_base.FM.sound_FM_pre import FM_pre_pulse077
from sound_base.FM.sound_FM_pre import FM_pre_saw
from sound_base.FM.sound_FM_pre import FM_pre_tri
from sound_base.FM.sound_FM_pre import FM_pre_isekai_church

def set_sound(note, sound_a, sampling, duration):

    # 異世界チャーチベルの倍音構造
    FM_pre_isekai_church()

    # 1オクターブ上げて透明感
    sa = FM_pre_sound(note + 12, sound_a, sampling, duration)

    # 金属の立ち上がりは硬め
    set_FME_solid()
    sa = set_FME(sa, duration)

    # 高周波ノイズを少量追加（粉っぽい金属）
    noise = CNoiseFreq(sound_a, duration, Freq(sound_a, note)*3, 0.3, sampling) * 0.05
    noise = set_FME(noise, duration)
    sa = sa + noise

    # 時間軸変形で “異世界の揺れ”
    mod = SINFreq(sound_a, duration, Freq(sound_a, note)/2, 0.01, 0.0, sampling)
    sa = Modulate(sa, mod, 0.03, 0.2)

    return limitter(sa)
