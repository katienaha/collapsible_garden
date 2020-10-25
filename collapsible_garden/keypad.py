
import adafruit_matrixkeypad
from digitalio import DigitalInOut
import board
import time

# Keypad for entering user input
class Keypad:

    def __init__(self, rows, cols):
        
        keys = ((1, 2, 3),
                (4, 5, 6),
                (7, 8, 9),
                ('*', 0, '#'))

        self.keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

    def receive_input(self, quit_char, lcd):
        
        
        keys = []
        input_str = ''
        while quit_char not in keys:
            keys = self.keypad.pressed_keys
            for k in keys:
                input_str = input_str + str(k)
                
                lcd.display_text(lcd.last_message + str(k))
                time.sleep(0.5)
            time.sleep(0.01)
            
        return input_str




