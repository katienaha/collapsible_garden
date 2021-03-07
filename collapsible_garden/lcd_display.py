
import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd
import time

# LCD that displays initial questions, keypad entries, and status
class LcdDisplay:

    def __init__(self, pins, columns=16, rows=2):
        self.pins = pins
        self.columns = columns
        self.rows = rows
        
        lcd_rs = digitalio.DigitalInOut(pins['rs'])
        lcd_en = digitalio.DigitalInOut(pins['en'])
        lcd_d7 = digitalio.DigitalInOut(pins['d7'])
        lcd_d6 = digitalio.DigitalInOut(pins['d6'])
        lcd_d5 = digitalio.DigitalInOut(pins['d5'])
        lcd_d4 = digitalio.DigitalInOut(pins['d4'])

        lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, columns, rows)
        lcd.message = "Hello Katie"

        
#        lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5,
#                                                    lcd_d6, lcd_d7, columns, rows)
#        lcd.message = "Hello Kelsey!"
        last_message = ''
        self.lcd = lcd
        #time.sleep(5)

    def display_text(self, message):
        print('Displaying message: {}'.format(message))
        self.lcd.clear()
        time.sleep(0.1)
        self.lcd.message = message
        self.last_message = self.lcd.message 
