import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
# from kmk.scanners import DiodeOrientation

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

# keyboard.col_pins = (board.GP26,)
# keyboard.row_pins = (board.GP1,)
# keyboard.diode_orientation = DiodeOrientation.COL2ROW

