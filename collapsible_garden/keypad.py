
import adafruit_matrixkeypad
from digitalio import DigitalInOut
import board

# Keypad for entering user input
class Keypad:

    def __init__(self, pins):
        self.pins = pins

        # Classic 3x4 matrix keypad
        cols = [DigitalInOut(x) for x in (board.D2, board.D0, board.D4)]
        rows = [DigitalInOut(x) for x in (board.D1, board.D6, board.D5, board.D3)]
        keys = ((1, 2, 3),
                (4, 5, 6),
                (7, 8, 9),
                ('*', 0, '#'))

        keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

    def receive_input(self):
        keys = keypad.pressed_keys
        return keys




