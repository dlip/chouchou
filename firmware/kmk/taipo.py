try:
    from typing import Optional, Tuple, Union
except ImportError:
    pass
from micropython import const

import kmk.handlers.stock as handlers
from kmk.keys import Key, make_key
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules import Module
from kmk.utils import Debug

debug = Debug(__name__)

taipo_keycodes = {
    'TP_TLP': 0,
    'TP_TLR': 1,
    'TP_TLM': 2,
    'TP_TLI': 3,
    'TP_BLP': 4,
    'TP_BLR': 5,
    'TP_BLM': 6,
    'TP_BLI': 7,
    'TP_LIT': 8,
    'TP_LOT': 9,
    'TP_TRP': 10,
    'TP_TRR': 11,
    'TP_TRM': 12,
    'TP_TRI': 13,
    'TP_BRP': 14,
    'TP_BRR': 15,
    'TP_BRM': 16,
    'TP_BRI': 17,
    'TP_RIT': 18,
    'TP_ROT': 19,
    'KC_LAYER0': 20,
    'KC_LAYER1': 21,
    'KC_LAYER2': 22,
    'KC_LAYER3': 23,
    'KC_MOD_GA': 24,
    'KC_MOD_GC': 25,
    'KC_MOD_GS': 26,
    'KC_MOD_AC': 27,
    'KC_MOD_AS': 28,
    'KC_MOD_CS': 29,
    'KC_MOD_GAC': 30,
    'KC_MOD_GAS': 31,
    'KC_MOD_GCS': 32,
    'KC_MOD_ACS': 33,
    'KC_MOD_GACS': 34,
};

class KeyPress:
    keycode = 0
    hold = False
    hold_handled = False
    
class State:
    combo = 0
    timer = 0
    keypress: KeyPress

class TaipoMeta:
    def __init__(self, code):
        self.code = code
    
class Taipo(Module):
    def __init__(self):
        for key, code in taipo_keycodes.items():
            make_key( names=(key,), meta=TaipoMeta(code))

    def during_bootup(self, keyboard):
        pass

    def before_matrix_scan(self, keyboard):
        pass

    def after_matrix_scan(self, keyboard):
        pass

    def process_key(self, keyboard, key, is_pressed, int_coord):
        debug('hi')
        if debug.enabled:
            debug('activate', key.meta.code)
        return key

    def before_hid_send(self, keyboard):
        pass

    def after_hid_send(self, keyboard):
        pass

    def on_powersave_enable(self, keyboard):
        pass

    def on_powersave_disable(self, keyboard):
        pass

