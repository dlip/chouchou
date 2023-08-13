try:
    from typing import Optional, Tuple, Union
except ImportError:
    pass
from micropython import const

import kmk.handlers.stock as handlers
from kmk.keys import Key, KC, make_key
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules import Module
from kmk.utils import Debug
from supervisor import ticks_ms

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
    'LAYER0': 20,
    'LAYER1': 21,
    'LAYER2': 22,
    'LAYER3': 23,
    'MOD_GA': 24,
    'MOD_GC': 25,
    'MOD_GS': 26,
    'MOD_AC': 27,
    'MOD_AS': 28,
    'MOD_CS': 29,
    'MOD_GAC': 30,
    'MOD_GAS': 31,
    'MOD_GCS': 32,
    'MOD_ACS': 33,
    'MOD_GACS': 34,
};

r = 1 << 0
s = 1 << 1
n = 1 << 2
i = 1 << 3
a = 1 << 4
o = 1 << 5
t = 1 << 6
e = 1 << 7
it = 1 << 8
ot = 1 << 9

class KeyPress:
    keycode = KC.NO
    hold = False
    hold_handled = False
    
class State:
    combo = 0
    timer = 0
    key = KeyPress()

class TaipoMeta:
    def __init__(self, code):
        self.taipo_code = code
    
class Taipo(Module):
    def __init__(self, tap_timeout=150, sticky_timeout=1000):
        self.tap_timeout = tap_timeout
        self.sticky_timeout=sticky_timeout
        self.state = [State(), State()]
        for key, code in taipo_keycodes.items():
            make_key( names=(key,), meta=TaipoMeta(code))

        self.keymap = {
            t: KC.T,
            t | e: KC.H,
            it: KC.BSPC,
            ot: KC.SPC,
            r: KC.R,
            r | ot: KC.LSFT(KC.R),
            r | it: KC.RABK,
            r | ot | it: KC.PRINT_SCREEN,
            s: KC.S,
            s | ot: KC.LSFT(KC.S),
            s | it: KC.RCBR,
            s | ot | it: KC.BRIGHTNESS_UP,
            n: KC.N,
            n | ot: KC.LSFT(KC.N),
            n | it: KC.RBRC,
            n | ot | it: KC.BRIGHTNESS_DOWN,
            i: KC.I,
            i | ot: KC.LSFT(KC.I),
            i | it: KC.RPRN,
            i | ot | it: KC.MEDIA_PLAY_PAUSE,
            a: KC.A,
            a | ot: KC.LSFT(KC.A),
            a | it: KC.LABK,
            a | ot | it: KC.MEDIA_NEXT_TRACK,
            o: KC.O,
            o | ot: KC.LSFT(KC.O),
            o | it: KC.LCBR,
            o | ot | it: KC.AUDIO_VOL_UP,
            t: KC.T,
            t | ot: KC.LSFT(KC.T),
            t | it: KC.LBRC,
            t | ot | it: KC.AUDIO_VOL_DOWN,
            e: KC.E,
            e | ot: KC.LSFT(KC.E),
            e | it: KC.LPRN,
            e | ot | it: KC.MEDIA_PREV_TRACK,
            e | o: KC.C,
            e | o | ot: KC.LSFT(KC.C),
            e | o | it: KC.N1,
            e | o | ot | it: KC.F1,
            t | o: KC.U,
            t | o | ot: KC.LSFT(KC.U),
            t | o | it: KC.N2,
            t | o | ot | it: KC.F2,
            t | a: KC.Q,
            t | a | ot: KC.LSFT(KC.Q),
            t | a | it: KC.N3,
            t | a | ot | it: KC.F3,
            o | a: KC.L,
            o | a | ot: KC.LSFT(KC.L),
            o | a | it: KC.N4,
            o | a | ot | it: KC.F4,
            i | n: KC.Y,
            i | n | ot: KC.LSFT(KC.Y),
            i | n | it: KC.N5,
            i | n | ot | it: KC.F5,
            i | s: KC.F,
            i | s | ot: KC.LSFT(KC.F),
            i | s | it: KC.N6,
            i | s | ot | it: KC.F6,
            n | s: KC.P,
            n | s | ot: KC.LSFT(KC.P),
            n | s | it: KC.N7,
            n | s | ot | it: KC.F7,
            n | r: KC.Z,
            n | r | ot: KC.LSFT(KC.Z),
            n | r | it: KC.N8,
            n | r | ot | it: KC.F8,
            s | r: KC.B,
            s | r | ot: KC.LSFT(KC.B),
            s | r | it: KC.N9,
            s | r | ot | it: KC.F9,
            e | t: KC.H,
            e | t | ot: KC.LSFT(KC.H),
            e | t | it: KC.N0,
            e | t | ot | it: KC.F10,
            e | a: KC.D,
            e | a | ot: KC.LSFT(KC.D),
            e | a | it: KC.AT,
            e | a | ot | it: KC.F11,
            i | r: KC.G,
            i | r | ot: KC.LSFT(KC.G),
            i | r | it: KC.HASH,
            i | r | ot | it: KC.F12,
            t | r: KC.X,
            t | r | ot: KC.LSFT(KC.X),
            t | r | it: KC.CIRC,
            t | r | ot | it: KC.LCTL(KC.X),
            i | o: KC.K,
            i | o | ot: KC.LSFT(KC.K),
            i | o | it: KC.PLUS,
            i | o | ot | it: KC.LCTL(KC.C),
            e | s: KC.V,
            e | s | ot: KC.LSFT(KC.V),
            e | s | it: KC.ASTR,
            e | s | ot | it: KC.LCTL(KC.V),
            n | a: KC.J,
            n | a | ot: KC.LSFT(KC.J),
            n | a | it: KC.EQL,
            n | a | ot | it: KC.LCTL(KC.Z),
            e | r: KC.M,
            e | r | ot: KC.LSFT(KC.M),
            e | r | it: KC.DLR,
            # e | r | ot | it: KC.NO,
            i | a: KC.W,
            i | a | ot: KC.LSFT(KC.W),
            i | a | it: KC.AMPR,
            # i | a | ot | it: KC.NO,
            t | s: KC.SLSH,
            t | s | ot: KC.BSLS,
            t | s | it: KC.PIPE,
            # t | s | ot | it: KC.NO,
            n | o: KC.MINS,
            n | o | ot: KC.UNDS,
            n | o | it: KC.PERC,
            # n | o | ot | it: KC.NO,
            i | t: KC.QUES,
            i | t | ot: KC.EXLM,
            # i | t | it: KC.NO,
            # i | t | ot | it: KC.NO,
            e | n: KC.COMM,
            e | n | ot: KC.DOT,
            e | n | it: KC.TILD,
            # e | n | ot | it: KC.NO,
            o | r: KC.SCLN,
            t | o | a: KC.SCLN,
            o | r | ot: KC.COLN,
            t | o | a | ot: KC.COLN,
            # o | r | it: KC.NO,
            # t | o | a | it: KC.NO,
            # o | r | ot | it: KC.NO,
            # t | o | a | ot | it: KC.NO,
            s | a: KC.QUOT,
            n | s | r: KC.QUOT,
            s | a | ot: KC.DQT,
            n | s | r | ot: KC.DQT,
            s | a | it: KC.GRV,
            n | s | r | it: KC.GRV,
            # s | a | ot | it: KC.NO,
            # n | s | r | ot | it: KC.NO,
            i | n | s: KC.TAB,
            i | n | s | ot: KC.DEL,
            i | n | s | it: KC.INS,
            # i | n | s | ot | it: KC.NO,
            e | t | o: KC.ENTER,
            e | t | o | ot: KC.ESC,
            e | t | o | it: KC.RALT,
            # e | t | o | ot | it: KC.NO,
            a | r: KC.LGUI,
            a | r | ot: KC.RIGHT,
            a | r | it: KC.PGUP,
            a | r | ot | it: KC.LAYER3,
            o | s: KC.LALT,
            o | s | ot: KC.UP,
            o | s | it: KC.HOME,
            o | s | ot | it: KC.LAYER2,
            t | n: KC.LCTL,
            t | n | ot: KC.DOWN,
            t | n | it: KC.END,
            t | n | ot | it: KC.LAYER1,
            e | i: KC.LSFT,
            e | i | ot: KC.LEFT,
            e | i | it: KC.PGDN,
            e | i | ot | it: KC.LAYER0,
            r | a | s | o: KC.MOD_GA,
            r | a | n | t: KC.MOD_GC,
            r | a | i | e: KC.MOD_GS,
            s | o | n | t: KC.MOD_AC,
            s | o | i | e: KC.MOD_AS,
            n | t | i | e: KC.MOD_CS,
            r | a | s | o | n | t: KC.MOD_GAC,
            r | a | s | o | i | e: KC.MOD_GAS,
            r | a | n | t | i | e: KC.MOD_GCS,
            s | o | n | t | i | e: KC.MOD_ACS,
            r | a | s | o | n | t | i | e: KC.MOD_GACS,
        }

    def during_bootup(self, keyboard):
        pass

    def before_matrix_scan(self, keyboard):
        for side in [0, 1]:
            if self.state[side].timer != 0 and ticks_ms() > self.state[side].timer:
                self.state[side].key.keycode = self.determine_key(self.state[side].combo)
                self.state[side].key.hold = True
                self.handle_key(keyboard, side)
                self.state[side].timer = 0

    def after_matrix_scan(self, keyboard):
        pass

    def process_key(self, keyboard, key, is_pressed, int_coord):
        if hasattr(key.meta, 'taipo_code'):
            side = 1 if key.meta.taipo_code / 10 >= 1 else 0
            code = key.meta.taipo_code
            if is_pressed:
                if self.state[side].key.keycode != KC.NO:
                    self.handle_key(keyboard, side)
                    self.clear_state(side)
                
                self.state[side].combo |= 1 << (key.meta.taipo_code % 10)
                self.state[side].timer = ticks_ms() + self.tap_timeout
            else:
                if not self.state[side].key.hold:
                    self.state[side].key.keycode = self.determine_key(self.state[side].combo)
                self.handle_key(keyboard, side)
                self.clear_state(side)
        else:
            return key

    def clear_state(self, side):
        # why does this not work?
        # self.state[side] = State()
        self.state[side].combo = 0
        self.state[side].timer = 0
        self.state[side].key.keycode = KC.NO
        self.state[side].key.hold = False
        self.state[side].key.hold_handled = False
        
    def handle_key(self, keyboard, side):
        key = self.state[side].key
        mods = []

        if key.keycode in [ KC.LGUI, KC.LALT, KC.RALT, KC.LCTL, KC.LSFT ]:
            mods = [key.keycode]
        elif key.keycode == KC.MOD_GA:
            mods = [KC.LGUI, KC.LALT]
        elif key.keycode == KC.MOD_GC:
            mods = [KC.LGUI,KC.LCTL]
        elif key.keycode == KC.MOD_GS:
            mods = [KC.LGUI,KC.LSFT]
        elif key.keycode == KC.MOD_AC:
            mods = [KC.LALT,KC.LSFT]
        elif key.keycode == KC.MOD_AS:
            mods = [KC.LALT,KC.LSFT]
        elif key.keycode == KC.MOD_CS:
            mods = [KC.LCTL,KC.LSFT]
        elif key.keycode == KC.MOD_GAC:
            mods = [KC.LGUI,KC.LALT,KC.LSFT]
        elif key.keycode == KC.MOD_GAS:
            mods = [KC.LGUI,KC.LALT,KC.LSFT]
        elif key.keycode == KC.MOD_GCS:
            mods = [KC.LGUI,KC.LCTL,KC.LSFT]
        elif key.keycode == KC.MOD_ACS:
            mods = [KC.LALT,KC.LCTL,KC.LSFT]
        elif key.keycode == KC.MOD_GACS:
            mods = [KC.LGUI,KC.LALT,KC.LCTL,KC.LSFT]

        if len(mods) > 0:
            for mod in mods:
                if key.hold_handled:
                    keyboard.remove_key(mod)
                elif key.hold:
                    keyboard.add_key(mod)
                    self.state[side].key.hold_handled = True
                else:
                    keyboard.tap_key(KC.OS(mod, tap_time=self.sticky_timeout))
        else:
            if key.hold_handled:
                keyboard.remove_key(key.keycode)
            elif key.hold:
                keyboard.add_key(key.keycode)
                self.state[side].key.hold_handled = True
            else:
                keyboard.tap_key(key.keycode)
        
    def determine_key(self, val):
        if val in self.keymap:
            return self.keymap[val]
        else:
            return KC.NO
       
    def before_hid_send(self, keyboard):
        pass

    def after_hid_send(self, keyboard):
        pass

    def on_powersave_enable(self, keyboard):
        pass

    def on_powersave_disable(self, keyboard):
        pass

