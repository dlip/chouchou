import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner

class ChouChou(KMKKeyboard):

    def __init__(self):
        self.matrix = KeysScanner([
            board.GP26, board.GP27, board.GP28, board.GP29,   board.GP0, board.GP1, board.GP2, board.GP3,
            board.GP12, board.GP13, board.GP14, board.GP15,   board.GP4, board.GP5, board.GP6, board.GP7,
                                    board.GP11, board.GP10,   board.GP9, board.GP8,
        ])

