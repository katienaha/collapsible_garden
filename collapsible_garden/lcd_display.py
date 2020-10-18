
import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd

# LCD that displays initial questions, keypad entries, and status
class LcdDisplay:

    def __init__(self, pins, columns=16, rows=2):
        self.pins = pins
        self.columns = columns
        self.rows = rows
        self.lcd = character_lcd.Character_LCD_Mono(pins['rs'], pins['en'], pins['lcd_d4'], pins['lcd_d5'],
                                                    pins['lcd_d6'], pins['lcd_d7'], columns, rows,
                                                    pins['lcd_backlight'])

    def display_text(self, message):
        self.lcd.message = message
