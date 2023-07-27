print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
# from kmk.scanners import DiodeOrientation
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.scanners.keypad import KeysScanner
class ChouChou(KMKKeyboard):

    def __init__(self):
        self.matrix = KeysScanner([
            board.GP26, board.GP27, board.GP28, board.GP29,   board.GP0, board.GP1, board.GP2, board.GP3,
            board.GP12, board.GP13, board.GP14, board.GP15,   board.GP4, board.GP5, board.GP6, board.GP7,
                                    board.GP11, board.GP10,   board.GP9, board.GP8,
        ])

    # coord_mapping = [
    #  0,  1,  2,  3,   4,  5,  6,  7,
    #  8,  9, 10, 11,  12, 13, 14, 15,
    #         16, 17,  18, 19
    # ]

keyboard = ChouChou()

combos = Combos()
keyboard.modules.append(combos)


timeout = 100
combos.combos = [
    # Chord((KC.N, KC.I), KC.Y, timeout=timeout),
    Chord((2, 3), KC.Y, match_coord=True, timeout=timeout),
    Chord((4, 5), KC.Y, match_coord=True, timeout=timeout),
]
# keyboard.col_pins = (board.GP26,)
# keyboard.row_pins = (board.GP1,)
# keyboard.diode_orientation = DiodeOrientation.COL2ROW

    # [0] = LAYOUT_split_2x4_2(
    #     KC_R,    KC_S,    KC_N,    KC_I,        KC_I,    KC_N,    KC_S,    KC_R,
    #     KC_A,    KC_O,    KC_T,    KC_E,        KC_E,    KC_T,    KC_O,    KC_A,
    #                       KC_BSPC, KC_SPC,      KC_SPC,  KC_BSPC
    # )
keyboard.keymap = [
    [ KC.R, KC.S, KC.N, KC.I,    KC.N, KC.I, KC.S, KC.R,
     KC.A, KC.O, KC.T, KC.E,    KC.E, KC.T, KC.O, KC.A ,
                 KC.BSPC, KC.SPC,    KC.SPC, KC.BSPC             ,

]]




if __name__ == '__main__':
    keyboard.go()