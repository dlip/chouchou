print("Starting")

from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.modules.oneshot import OneShot

from kb import ChouChou
from taipo import Taipo

keyboard = ChouChou()

keyboard.debug_enabled = True
keyboard.extensions.append(MediaKeys())

taipo = Taipo()
keyboard.modules.append(taipo)
oneshot = OneShot()
keyboard.modules.append(oneshot)

keyboard.keymap = [
    [  KC.TP_TLP,        KC.TP_TLR,    KC.TP_TLM,       KC.TP_TLI,          KC.TP_TRI,     KC.TP_TRM,     KC.TP_TRR,     KC.TP_TRP,
       KC.TP_BLP,        KC.TP_BLR,    KC.TP_BLM,       KC.TP_BLI,          KC.TP_BRI,     KC.TP_BRM,     KC.TP_BRR,     KC.TP_BRP,
                                 KC.TP_LIT,       KC.TP_LOT,          KC.TP_ROT,     KC.TP_RIT,
]]

if __name__ == '__main__':
    keyboard.go()