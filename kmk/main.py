print("Starting")

from kmk.extensions.media_keys import MediaKeys
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.keys import KC
from kmk.modules.oneshot import OneShot

from kb import ChouChou

keyboard = ChouChou()

# keyboard.debug_enabled = True
keyboard.extensions.append(MediaKeys())

combos = Combos()
keyboard.modules.append(combos)
oneshot = OneShot()
keyboard.modules.append(oneshot)

timeout = 100

TLP = 0
TLR = 1
TLM = 2
TLI = 3
TRI = 4
TRM = 5
TRR = 6
TRP = 7

BLP = 8
BLR = 9
BLM = 10
BLI = 11
BRI = 12
BRM = 13
BRR = 14
BRP = 15

LIT = 16
LOT = 17
ROT = 18
RIT = 19

def make_combo(output, outer, inner, both, keys):
    combos = [
        Chord(keys + (KC.SPC,), outer, timeout=timeout),
        Chord(keys + (KC.BSPC,), inner, timeout=timeout),
    ]

    if (both != KC.NO):
        combos.append(Chord(keys + (KC.BSPC,KC.SPC), both, match_coord=True, timeout=timeout))

    if (len(keys) > 1):
        combos.append(Chord(keys, output, timeout=timeout)),

    return combos

taipo_combos = [
    # make_combo(KC.R,      KC.LSFT(KC.R), KC.RABK,    KC.PSCR,    (KC.R,),
        make_combo(KC.S,      KC.LSFT(KC.S), KC.RCBR,   KC.BRIU, (KC.S,)),
        make_combo(KC.N,      KC.LSFT(KC.N), KC.RBRC,   KC.BRID, (KC.N,)),
        make_combo(KC.I,      KC.LSFT(KC.I), KC.RPRN,   KC.MPLY,     (KC.I,)),
        make_combo(KC.A,      KC.LSFT(KC.A), KC.LABK,   KC.MNXT,   (KC.A,)),
        make_combo(KC.O,      KC.LSFT(KC.O), KC.LCBR,   KC.VOLU, (KC.O,)),
        make_combo(KC.T,      KC.LSFT(KC.T), KC.LBRC,   KC.VOLD, (KC.T,)),
        make_combo(KC.E,      KC.LSFT(KC.E), KC.LPRN,   KC.MPRV,   (KC.E,)),
        make_combo(KC.C,      KC.LSFT(KC.C), KC.N1,     KC.F1,       (KC.O, KC.E)),
        make_combo(KC.U,      KC.LSFT(KC.U), KC.N2,     KC.F2,       (KC.O, KC.T)),
        make_combo(KC.Q,      KC.LSFT(KC.Q), KC.N3,     KC.F3,       (KC.A, KC.T)),
        make_combo(KC.L,      KC.LSFT(KC.L), KC.N4,     KC.F4,       (KC.A, KC.O)),
        make_combo(KC.Y,      KC.LSFT(KC.Y), KC.N5,     KC.F5,       (KC.N, KC.I)),
        make_combo(KC.F,      KC.LSFT(KC.F), KC.N6,     KC.F6,       (KC.S, KC.I)),
        make_combo(KC.P,      KC.LSFT(KC.P), KC.N7,     KC.F7,       (KC.S, KC.N)),
        make_combo(KC.Z,      KC.LSFT(KC.Z), KC.N8,     KC.F8,       (KC.R, KC.N)),
        make_combo(KC.B,      KC.LSFT(KC.B), KC.N9,     KC.F9,       (KC.R, KC.S)),
        make_combo(KC.H,      KC.LSFT(KC.H), KC.N0,     KC.F10,      (KC.T, KC.E)),
        make_combo(KC.D,      KC.LSFT(KC.D), KC.AT,     KC.F11,      (KC.A, KC.E)),
        make_combo(KC.G,      KC.LSFT(KC.G), KC.HASH,   KC.F12,      (KC.R, KC.I)),
        make_combo(KC.X,      KC.LSFT(KC.X), KC.CIRC,   KC.LCTL(KC.X), (KC.R, KC.T)),
        make_combo(KC.K,      KC.LSFT(KC.K), KC.PLUS,   KC.LCTL(KC.C), (KC.I, KC.O)),
        make_combo(KC.V,      KC.LSFT(KC.V), KC.PAST,   KC.LCTL(KC.V), (KC.S, KC.E)),
        make_combo(KC.J,      KC.LSFT(KC.J), KC.EQUAL,  KC.LCTL(KC.Z), (KC.N, KC.A)),
        make_combo(KC.M,      KC.LSFT(KC.M), KC.DOLLAR, KC.NO,       (KC.R, KC.E)),
        make_combo(KC.W,      KC.LSFT(KC.W), KC.AMPR,   KC.NO,       (KC.I, KC.A)),
        make_combo(KC.SLASH,  KC.BSLS,    KC.PIPE,   KC.NO,       (KC.S, KC.T)),
        make_combo(KC.MINUS,  KC.UNDS,    KC.PERC,   KC.NO,       (KC.N, KC.O)),
        make_combo(KC.QUES,   KC.EXLM,    KC.CAPS,   KC.NO,       (KC.I, KC.T)),
        make_combo(KC.COMMA,  KC.DOT,     KC.TILDE,  KC.NO,       (KC.N, KC.E)),
        # make_combo(KC.SCLN,   KC.COLON,   KC.NO,     KC.NO,       (KC.R, KC.O)),
        make_combo(KC.SCLN,   KC.COLON,   KC.NO,     KC.NO,       (KC.O, KC.N, KC.E)),
        # make_combo(KC.QUOT,   KC.DQT,     KC.GRAVE,  KC.NO,       (KC.S, KC.A)),
        make_combo(KC.QUOT,   KC.DQT,     KC.GRAVE,  KC.NO,       (KC.O, KC.N, KC.I)),
        make_combo(KC.TAB,    KC.DEL,     KC.INS,    KC.NO,       (KC.S, KC.N, KC.I)),
        make_combo(KC.ENTER,  KC.ESC,     KC.LALT,   KC.NO,       (KC.O, KC.T, KC.E)),
        make_combo(KC.OS(KC.LGUI, tap_time=None),   KC.RIGHT, KC.PGUP,   KC.NO,        (KC.R, KC.A)),
        make_combo(KC.OS(KC.LALT, tap_time=None),   KC.UP,    KC.HOME,   KC.NO,        (KC.S, KC.O)),
        make_combo(KC.OS(KC.LCTL, tap_time=None),  KC.DOWN,  KC.END,    KC.NO,        (KC.N, KC.T)),
        make_combo(KC.OS(KC.LSFT, tap_time=None), KC.LEFT,  KC.PGDN,   KC.NO,        (KC.I, KC.E))
]

combos.combos = [item for sublist in taipo_combos for item in sublist]
print(len(combos.combos))
# combos.combos = [
#     Chord((0, 1), KC.A, match_coord=True),
# ]

# keyboard.keymap = [
#     [ KC.NO, KC.NO, KC.NO, KC.NO,    KC.NO, KC.NO, KC.NO, KC.NO,
#      KC.NO, KC.NO, KC.NO, KC.NO,    KC.NO, KC.NO, KC.NO, KC.NO ,
#                  KC.NO, KC.NO,    KC.NO, KC.NO             ,

# ]]
keyboard.keymap = [
    [ KC.R, KC.S, KC.N, KC.I,    KC.I, KC.N, KC.S, KC.R,
     KC.A, KC.O, KC.T, KC.E,    KC.E, KC.T, KC.O, KC.A ,
                 KC.BSPC, KC.SPC,    KC.SPC, KC.BSPC             ,
]]

if __name__ == '__main__':
    keyboard.go()