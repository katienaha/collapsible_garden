
from datetime import datetime

config = dict()

# Default time to turn light on in the morning
config['light_start_time'] = datetime(2020, 1, 1, 7, 0, 0)

# Default number of hours to leave the light on
config['light_duration_hrs'] = 16

# Default current date
config['current_date'] = datetime(2020, 1, 1)

# TODO: The following pin numbers are placeholders
# Pin Definitons:
config['lcd_pins'] = {'rs': 11,
                      'en': 12,
                      'd4': 13,
                      'd5': 14,
                      'd6': 15,
                      'd7': 16,
                      'backlight': 17}
config['led_pins'] = [25, 26]
config['keypad_pins'] = [18, 19, 20, 21, 22]
config['relay_pins'] = [23, 24]
