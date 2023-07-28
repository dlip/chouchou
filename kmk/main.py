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

def make_combo(output, outer, inner, both, leftpos, rightpos):
    combos = [
        Chord(leftpos + (LOT,), outer, match_coord=True, timeout=timeout),
        Chord(rightpos + (ROT,), outer, match_coord=True, timeout=timeout),
        Chord(leftpos + (LIT,), inner, match_coord=True, timeout=timeout),
        Chord(rightpos + (RIT,), inner, match_coord=True, timeout=timeout),
    ]

    if (both != KC.NO):
        combos.append(Chord(leftpos + (LIT,LOT), both, match_coord=True, timeout=timeout))
        combos.append(Chord(rightpos + (ROT,RIT), both, match_coord=True, timeout=timeout))

    if (len(leftpos) > 1):
        combos.append(Chord(leftpos, output, match_coord=True, timeout=timeout)),

    if (len(rightpos) > 1):
        combos.append(Chord(rightpos, output, match_coord=True, timeout=timeout)),

    return combos

taipo_combos = [
    # make_combo(KC.R,      KC.LSFT(KC.R), KC.RABK,    KC.PSCR,    (TLP,),         (TRP,)),
    make_combo(KC.S,      KC.LSFT(KC.S), KC.RCBR,   KC.BRIU, (TLR,),         (TRR,)),
    make_combo(KC.N,      KC.LSFT(KC.N), KC.RBRC,   KC.BRID, (TLM,),         (TRM,)),
    make_combo(KC.I,      KC.LSFT(KC.I), KC.RPRN,   KC.MPLY,     (TLI,),         (TRI,)),
    make_combo(KC.A,      KC.LSFT(KC.A), KC.LABK,   KC.MNXT,   (BLP,),         (BRP,)),
    make_combo(KC.O,      KC.LSFT(KC.O), KC.LCBR,   KC.VOLU, (BLR,),         (BRR,)),
    make_combo(KC.T,      KC.LSFT(KC.T), KC.LBRC,   KC.VOLD, (BLM,),         (BRM,)),
    make_combo(KC.E,      KC.LSFT(KC.E), KC.LPRN,   KC.MPRV,   (BLI,),         (BRI,)),
    make_combo(KC.C,      KC.LSFT(KC.C), KC.N1,     KC.F1,       (BLR, BLI),     (BRR, BRI)),
    make_combo(KC.U,      KC.LSFT(KC.U), KC.N2,     KC.F2,       (BLR, BLM),     (BRR, BRM)),
    make_combo(KC.Q,      KC.LSFT(KC.Q), KC.N3,     KC.F3,       (BLP, BLM),     (BRP, BRM)),
    make_combo(KC.L,      KC.LSFT(KC.L), KC.N4,     KC.F4,       (BLP, BLR),     (BRP, BRR)),
    make_combo(KC.Y,      KC.LSFT(KC.Y), KC.N5,     KC.F5,       (TLM, TLI),     (TRM, TRI)),
    make_combo(KC.F,      KC.LSFT(KC.F), KC.N6,     KC.F6,       (TLR, TLI),     (TRR, TRI)),
    make_combo(KC.P,      KC.LSFT(KC.P), KC.N7,     KC.F7,       (TLR, TLM),     (TRR, TRM)),
    make_combo(KC.Z,      KC.LSFT(KC.Z), KC.N8,     KC.F8,       (TLP, TLM),     (TRP, TRM)),
    make_combo(KC.B,      KC.LSFT(KC.B), KC.N9,     KC.F9,       (TLP, TLR),     (TRP, TRR)),
    make_combo(KC.H,      KC.LSFT(KC.H), KC.N0,     KC.F10,      (BLM, BLI),     (BRM, BRI)),
    make_combo(KC.D,      KC.LSFT(KC.D), KC.AT,     KC.F11,      (BLP, BLI),     (BRP, BRI)),
    make_combo(KC.G,      KC.LSFT(KC.G), KC.HASH,   KC.F12,      (TLP, TLI),     (TRP, TRI)),
    make_combo(KC.X,      KC.LSFT(KC.X), KC.CIRC,   KC.LCTL(KC.X), (TLP, BLM),     (TRP, BRM)),
    make_combo(KC.K,      KC.LSFT(KC.K), KC.PLUS,   KC.LCTL(KC.C), (TLI, BLR),     (TRI, BRR)),
    make_combo(KC.V,      KC.LSFT(KC.V), KC.PAST,   KC.LCTL(KC.V), (TLR, BLI),     (TRR, BRI)),
    make_combo(KC.J,      KC.LSFT(KC.J), KC.EQUAL,  KC.LCTL(KC.Z), (TLM, BLP),     (TRM, BRP)),
    make_combo(KC.M,      KC.LSFT(KC.M), KC.DOLLAR, KC.NO,       (TLP, BLI),     (TRP, BRI)),
    make_combo(KC.W,      KC.LSFT(KC.W), KC.AMPR,   KC.NO,       (TLI, BLP),     (TRI, BRP)),
    make_combo(KC.SLASH,  KC.BSLS,    KC.PIPE,   KC.NO,       (TLR, BLM),     (TRR, BRM)),
    make_combo(KC.MINUS,  KC.UNDS,    KC.PERC,   KC.NO,       (TLM, BLR),     (TRM, BRR)),
    make_combo(KC.QUES,   KC.EXLM,    KC.CAPS,   KC.NO,       (TLI, BLM),     (TRI, BRM)),
    make_combo(KC.COMMA,  KC.DOT,     KC.TILDE,  KC.NO,       (TLM, BLI),     (TRM, BRI)),
    make_combo(KC.SCLN,   KC.COLON,   KC.NO,     KC.NO,       (TLP, BLR),     (TRP, BRR)),
    make_combo(KC.SCLN,   KC.COLON,   KC.NO,     KC.NO,       (BLR, TLM, BLI), (BRR, TRM, BRI)),
    make_combo(KC.QUOT,   KC.DQT,     KC.GRAVE,  KC.NO,       (TLR, BLP),     (TRR, BRP)),
    make_combo(KC.QUOT,   KC.DQT,     KC.GRAVE,  KC.NO,       (BLR, TLM, TLI), (BRR, TRM, TRI)),
    make_combo(KC.TAB,    KC.DEL,     KC.INS,    KC.NO,       (TLR, TLM, TLI), (TRR, TRM, TRI)),
    make_combo(KC.ENTER,  KC.ESC,     KC.LALT,   KC.NO,       (BLR, BLM, BLI), (BRR, BRM, BRI)),
    make_combo(KC.OS(KC.LGUI, tap_time=None),   KC.RIGHT, KC.PGUP,   KC.NO,        (TLP, BLP),     (TRP, BRP)),
    make_combo(KC.OS(KC.LALT, tap_time=None),   KC.UP,    KC.HOME,   KC.NO,        (TLR, BLR),     (TRR, BRR)),
    make_combo(KC.OS(KC.LCTL, tap_time=None),  KC.DOWN,  KC.END,    KC.NO,        (TLM, BLM),     (TRM, BRM)),
    make_combo(KC.OS(KC.LSFT, tap_time=None), KC.LEFT,  KC.PGDN,   KC.NO,        (TLI, BLI),     (TRI, BRI)),
]

combos.combos = [item for sublist in taipo_combos for item in sublist]
# combos.combos = [
#     Chord((0, 1), KC.A, match_coord=True),
# ]

# keyboard.keymap = [
#     [ KC.NO, KC.NO, KC.NO, KC.NO,    KC.NO, KC.NO, KC.NO, KC.NO,
#      KC.NO, KC.NO, KC.NO, KC.NO,    KC.NO, KC.NO, KC.NO, KC.NO ,
#                  KC.NO, KC.NO,    KC.NO, KC.NO             ,

# ]]
keyboard.keymap = [
    [ KC.R, KC.S, KC.N, KC.I,    KC.N, KC.I, KC.S, KC.R,
     KC.A, KC.O, KC.T, KC.E,    KC.E, KC.T, KC.O, KC.A ,
                 KC.BSPC, KC.SPC,    KC.SPC, KC.BSPC             ,
]]

if __name__ == '__main__':
    keyboard.go()