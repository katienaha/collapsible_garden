
import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd

# LCD that displays initial questions, keypad entries, and status
class LcdDisplay:

    def __init__(self, pins, columns=16, rows=2):
        self.pins = pins
        self.columns = columns
        self.rows = rows
        print(pins)
        self.lcd = character_lcd.Character_LCD_Mono(pins['rs'], pins['en'], pins['d4'], pins['d5'],
                                                    pins['d6'], pins['d7'], columns, rows,
                                                    pins['backlight'])
        self.last_message = ''

    def display_text(self, message):
        self.lcd.message = message
        self.last_message = self.lcd.message
