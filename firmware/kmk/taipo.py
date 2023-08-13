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

keymap = {
    t: KC.T,
    t | e: KC.H,
}

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
    def __init__(self):
        self.left_state = State()
        self.right_state = State()
        for key, code in taipo_keycodes.items():
            make_key( names=(key,), meta=TaipoMeta(code))

    def during_bootup(self, keyboard):
        pass

    def before_matrix_scan(self, keyboard):
        pass

    def after_matrix_scan(self, keyboard):
        pass

    def process_key(self, keyboard, key, is_pressed, int_coord):
        if hasattr(key.meta, 'taipo_code'):
            state = self.right_state if key.meta.taipo_code / 10 >= 1 else self.left_state
            code = key.meta.taipo_code
            debug('activate', key.meta.taipo_code)
            debug('code', self.determine_key(key.meta.taipo_code))
            if is_pressed:
                state.combo |= 1 << (key.meta.taipo_code % 10)
                debug(state.combo)
            else:
                state.key.keycode = self.determine_key(state.combo)
                self.handle_key(keyboard, state.key)
                state = State()
                #self.clear_state(state)
               
        else:
            return key

    def clear_state(self, state):
        state = State()
        
    def handle_key(self, keyboard, key: KeyPress):
        keyboard.tap_key(key.keycode)
        
    def determine_key(self, val):
        debug('val', val)
        if val in keymap:
            return keymap[val]
        else:
            return KC.NO
        # match val:
        #     case it:
        #         return KC_BSPC;
        #     case ot:
        #         return KC_SPC;
        #     case r:
        #         return KC_R;
        #     case r | ot:
        #         return S(KC_R);
        #     case r | it:
        #         return KC_GT;
        #     case r | ot | it:
        #         return KC_PRINT_SCREEN;
        #     case s:
        #         return KC_S;
        #     case s | ot:
        #         return S(KC_S);
        #     case s | it:
        #         return KC_RCBR;
        #     case s | ot | it:
        #         return KC_BRIGHTNESS_UP;
        #     case n:
        #         return KC_N;
        #     case n | ot:
        #         return S(KC_N);
        #     case n | it:
        #         return KC_RBRC;
        #     case n | ot | it:
        #         return KC_BRIGHTNESS_DOWN;
        #     case i:
        #         return KC_I;
        #     case i | ot:
        #         return S(KC_I);
        #     case i | it:
        #         return KC_RPRN;
        #     case i | ot | it:
        #         return KC_MEDIA_PLAY_PAUSE;
        #     case a:
        #         return KC_A;
        #     case a | ot:
        #         return S(KC_A);
        #     case a | it:
        #         return KC_LT;
        #     case a | ot | it:
        #         return KC_MEDIA_NEXT_TRACK;
        #     case o:
        #         return KC_O;
        #     case o | ot:
        #         return S(KC_O);
        #     case o | it:
        #         return KC_LCBR;
        #     case o | ot | it:
        #         return KC_KB_VOLUME_UP;
        #     case t:
        #         return KC_T;
        #     case t | ot:
        #         return S(KC_T);
        #     case t | it:
        #         return KC_LBRC;
        #     case t | ot | it:
        #         return KC_KB_VOLUME_DOWN;
        #     case e:
        #         return KC_E;
        #     case e | ot:
        #         return S(KC_E);
        #     case e | it:
        #         return KC_LPRN;
        #     case e | ot | it:
        #         return KC_MEDIA_PREV_TRACK;
        #     case e | o:
        #         return KC_C;
        #     case e | o | ot:
        #         return S(KC_C);
        #     case e | o | it:
        #         return KC_1;
        #     case e | o | ot | it:
        #         return KC_F1;
        #     case t | o:
        #         return KC_U;
        #     case t | o | ot:
        #         return S(KC_U);
        #     case t | o | it:
        #         return KC_2;
        #     case t | o | ot | it:
        #         return KC_F2;
        #     case t | a:
        #         return KC_Q;
        #     case t | a | ot:
        #         return S(KC_Q);
        #     case t | a | it:
        #         return KC_3;
        #     case t | a | ot | it:
        #         return KC_F3;
        #     case o | a:
        #         return KC_L;
        #     case o | a | ot:
        #         return S(KC_L);
        #     case o | a | it:
        #         return KC_4;
        #     case o | a | ot | it:
        #         return KC_F4;
        #     case i | n:
        #         return KC_Y;
        #     case i | n | ot:
        #         return S(KC_Y);
        #     case i | n | it:
        #         return KC_5;
        #     case i | n | ot | it:
        #         return KC_F5;
        #     case i | s:
        #         return KC_F;
        #     case i | s | ot:
        #         return S(KC_F);
        #     case i | s | it:
        #         return KC_6;
        #     case i | s | ot | it:
        #         return KC_F6;
        #     case n | s:
        #         return KC_P;
        #     case n | s | ot:
        #         return S(KC_P);
        #     case n | s | it:
        #         return KC_7;
        #     case n | s | ot | it:
        #         return KC_F7;
        #     case n | r:
        #         return KC_Z;
        #     case n | r | ot:
        #         return S(KC_Z);
        #     case n | r | it:
        #         return KC_8;
        #     case n | r | ot | it:
        #         return KC_F8;
        #     case s | r:
        #         return KC_B;
        #     case s | r | ot:
        #         return S(KC_B);
        #     case s | r | it:
        #         return KC_9;
        #     case s | r | ot | it:
        #         return KC_F9;
        #     case e | t:
        #         return KC_H;
        #     case e | t | ot:
        #         return S(KC_H);
        #     case e | t | it:
        #         return KC_0;
        #     case e | t | ot | it:
        #         return KC_F10;
        #     case e | a:
        #         return KC_D;
        #     case e | a | ot:
        #         return S(KC_D);
        #     case e | a | it:
        #         return KC_AT;
        #     case e | a | ot | it:
        #         return KC_F11;
        #     case i | r:
        #         return KC_G;
        #     case i | r | ot:
        #         return S(KC_G);
        #     case i | r | it:
        #         return KC_HASH;
        #     case i | r | ot | it:
        #         return KC_F12;
        #     case t | r:
        #         return KC_X;
        #     case t | r | ot:
        #         return S(KC_X);
        #     case t | r | it:
        #         return KC_CIRC;
        #     case t | r | ot | it:
        #         return C(KC_X);
        #     case i | o:
        #         return KC_K;
        #     case i | o | ot:
        #         return S(KC_K);
        #     case i | o | it:
        #         return KC_PLUS;
        #     case i | o | ot | it:
        #         return C(KC_C);
        #     case e | s:
        #         return KC_V;
        #     case e | s | ot:
        #         return S(KC_V);
        #     case e | s | it:
        #         return KC_ASTR;
        #     case e | s | ot | it:
        #         return C(KC_V);
        #     case n | a:
        #         return KC_J;
        #     case n | a | ot:
        #         return S(KC_J);
        #     case n | a | it:
        #         return KC_EQL;
        #     case n | a | ot | it:
        #         return C(KC_Z);
        #     case e | r:
        #         return KC_M;
        #     case e | r | ot:
        #         return S(KC_M);
        #     case e | r | it:
        #         return KC_DLR;
        #     // case e | r | ot | it:
        #     //     return KC_NO;
        #     case i | a:
        #         return KC_W;
        #     case i | a | ot:
        #         return S(KC_W);
        #     case i | a | it:
        #         return KC_AMPR;
        #     // case i | a | ot | it:
        #     //     return KC_NO;
        #     case t | s:
        #         return KC_SLSH;
        #     case t | s | ot:
        #         return KC_BSLS;
        #     case t | s | it:
        #         return KC_PIPE;
        #     // case t | s | ot | it:
        #     //     return KC_NO;
        #     case n | o:
        #         return KC_MINS;
        #     case n | o | ot:
        #         return KC_UNDS;
        #     case n | o | it:
        #         return KC_PERC;
        #     // case n | o | ot | it:
        #     //     return KC_NO;
        #     case i | t:
        #         return KC_QUES;
        #     case i | t | ot:
        #         return KC_EXLM;
        #     // case i | t | it:
        #     //     return KC_NO;
        #     // case i | t | ot | it:
        #     //     return KC_NO;
        #     case e | n:
        #         return KC_COMM;
        #     case e | n | ot:
        #         return KC_DOT;
        #     case e | n | it:
        #         return KC_TILD;
        #     // case e | n | ot | it:
        #     //     return KC_NO;
        #     case o | r:
        #     case t | o | a:
        #         return KC_SCLN;
        #     case o | r | ot:
        #     case t | o | a | ot:
        #         return KC_COLN;
        #     // case o | r | it:
        #     // case t | o | a | it:
        #     //     return KC_NO;
        #     // case o | r | ot | it:
        #     // case t | o | a | ot | it:
        #     //     return KC_NO;
        #     case s | a:
        #     case n | s | r:
        #         return KC_QUOT;
        #     case s | a | ot:
        #     case n | s | r | ot:
        #         return KC_DQT;
        #     case s | a | it:
        #     case n | s | r | it:
        #         return KC_GRV;
        #     // case s | a | ot | it:
        #     // case n | s | r | ot | it:
        #     //     return KC_NO;
        #     case i | n | s:
        #         return KC_TAB;
        #     case i | n | s | ot:
        #         return KC_DEL;
        #     case i | n | s | it:
        #         return KC_INS;
        #     // case i | n | s | ot | it:
        #     //     return KC_NO;
        #     case e | t | o:
        #         return KC_ENTER;
        #     case e | t | o | ot:
        #         return KC_ESC;
        #     case e | t | o | it:
        #         return KC_RALT;
        #     // case e | t | o | ot | it:
        #     //     return KC_NO;
        #     case a | r:
        #         return KC_LGUI;
        #     case a | r | ot:
        #         return KC_RIGHT;
        #     case a | r | it:
        #         return KC_PGUP;
        #     case a | r | ot | it:
        #         return KC_LAYER3;
        #     case o | s:
        #         return KC_LALT;
        #     case o | s | ot:
        #         return KC_UP;
        #     case o | s | it:
        #         return KC_HOME;
        #     case o | s | ot | it:
        #         return KC_LAYER2;
        #     case t | n:
        #         return KC_LCTL;
        #     case t | n | ot:
        #         return KC_DOWN;
        #     case t | n | it:
        #         return KC_END;
        #     case t | n | ot | it:
        #         return KC_LAYER1;
        #     case e | i:
        #         return KC_LSFT;
        #     case e | i | ot:
        #         return KC_LEFT;
        #     case e | i | it:
        #         return KC_PGDN;
        #     case e | i | ot | it:
        #         return KC_LAYER0;
        #     case r | a | s | o:
        #         return KC_MOD_GA;
        #     case r | a | n | t:
        #         return KC_MOD_GC;
        #     case r | a | i | e:
        #         return KC_MOD_GS;
        #     case s | o | n | t:
        #         return KC_MOD_AC;
        #     case s | o | i | e:
        #         return KC_MOD_AS;
        #     case n | t | i | e:
        #         return KC_MOD_CS;
        #     case r | a | s | o | n | t:
        #         return KC_MOD_GAC;
        #     case r | a | s | o | i | e:
        #         return KC_MOD_GAS;
        #     case r | a | n | t | i | e:
        #         return KC_MOD_GCS;
        #     case s | o | n | t | i | e:
        #         return KC_MOD_ACS;
        #     case r | a | s | o | n | t | i | e:
        #         return KC_MOD_GACS;
        # }
        # return KC_NO;

    def before_hid_send(self, keyboard):
        pass

    def after_hid_send(self, keyboard):
        pass

    def on_powersave_enable(self, keyboard):
        pass

    def on_powersave_disable(self, keyboard):
        pass

