
from datetime import datetime

config = dict()

# Default time to turn light on in the morning
config['light_start_time'] = datetime(2021, 1, 1, 7, 0, 0)

# Default number of hours to leave the light on
config['light_duration_hrs'] = 16

# Default current date
config['current_date'] = datetime(2021, 1, 1)

# TODO: The following pin numbers are placeholders
# Pin Definitons:
config['lcd_pins'] = {'rs': 2,
                      'en': 3,
                      'd4': 4,
                      'd5': 17,
                      'd6': 27,
                      'd7': 22,
                      'backlight': 10}
config['led_pins'] = [9, 11]
config['keypad_pins'] = [5, 6, 13, 19, 26]
config['relay_pins'] = [18]
config['water_sensor_pins'] = [23]
