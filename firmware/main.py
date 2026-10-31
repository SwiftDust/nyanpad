print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.macros import Macros, Press, Release, Tap

macros = Macros()
keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(macros)

keyboard.col_pins = (board.D1, board.D0)
keyboard.row_pins = (board.D3, board.D2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

OPEN_SPOTIFY = KC.MACRO(
    Press(KC.LCTL)
    Tap(KC.SPACE)
    Release(KC.LCTL)
    "spotify"
    Tap(KC.ENTER)
)

keyboard.keymap = [
    [KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN, KC.MEDIA_PLAY_PAUSE, OPEN_SPOTIFY]
]

if __name__ == '__main__':
    keyboard.go()
