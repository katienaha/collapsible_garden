
from datetime import datetime
import digitalio
import board

config = dict()

# Default time to turn light on in the morning
config['light_start_time'] = datetime(2021, 1, 1, 7, 0, 0)

# Default number of hours to leave the light on
config['light_duration_hrs'] = 16

# Default current date
config['current_date'] = datetime(2021, 1, 1)

# TODO: The following pin numbers are placeholders
# Pin Definitons:
config['lcd_pins'] = {'rs': board.D18,
                      'en': board.D23,
                      'd7': board.D24,
                      'd6': board.D25,
                      'd5': board.D8,
                      'd4': board.D7}

config['led_pins'] = {'water': 16,
                      'food' : 20}

config['keypad_cols'] = [digitalio.DigitalInOut(x) for x in (board.D26, board.D20, board.D21)]
config['keypad_rows'] = [digitalio.DigitalInOut(x) for x in (board.D5, board.D6, board.D13, board.D19)]
        
config['relay_pins'] = [5]
config['water_sensor_pins'] = [17]
