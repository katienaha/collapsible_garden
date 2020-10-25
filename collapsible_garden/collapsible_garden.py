"""Main module."""

from collapsible_garden import config
from collapsible_garden.grow_light import GrowLight
from collapsible_garden.keypad import Keypad
from collapsible_garden.lcd_display import LcdDisplay
from collapsible_garden.led_light import LedLight
from collapsible_garden.power_relay import PowerRelay
from collapsible_garden.water_level_sensor import WaterLevelSensor

# External module imports
import RPi.GPIO as GPIO
import time
from collapsible_garden import config
from datetime import datetime, timedelta
import re

class Garden:

    def __init__(self):
        # Retrieve Raspberry Pi pins for each component
        self.lcd_pins = config.config['lcd_pins']
        self.led_pins = config.config['led_pins']
        self.keypad_cols = config.config['keypad_cols']
        self.keypad_rows = config.config['keypad_rows']
        self.relay_pins = config.config['relay_pins']
        self.water_sensor_pins = config.config['water_sensor_pins']

        
        # Set up GPIO mode and pins to IN or OUT
        self.setup_pins()
        self.grow_light = GrowLight(self.relay_pins[0])
        self.keypad = Keypad(self.keypad_rows, self.keypad_cols)
        self.lcd_display = LcdDisplay(self.lcd_pins, columns=16, rows=2)
        self.led_light_water = LedLight(self.led_pins['water'])
        self.led_light_food = LedLight(self.led_pins['food'])
        self.power_relay = PowerRelay(self.relay_pins)
        self.water_level_sensor = WaterLevelSensor(self.water_sensor_pins[0])

        self.current_month = 1
        self.day_of_month = 1
        self.current_time = 1
        self.am_or_pm_current = 2
        self.light_start_time = 700
        self.am_or_pm_light_start = 1
        self.light_duration = 16
        self.feed_duration = timedelta(days=14)

        self.startup_pi_time = datetime.now()
        # Ask for user input upon startup
        self.request_input()

        # Change input times to 24 hour clock using AM and PM responses
        if self.am_or_pm_current == 2:
            self.current_time_int = self.current_time_int + 1200
        if self.am_or_pm_light_start == 2:
            self.light_start_time_int = self.current_time_int + 1200

        # Create datetime for when the user says the garden is starting
        self.user_start_datetime = datetime(2021, self.current_month, self.day_of_month,
                                      self.current_time_int // 100, self.current_time_int % 100)

        # Find difference between user-reported time and RPi's time
        self.clock_difference = self.user_start_datetime - self.startup_pi_time

        # Set up garden timing
        self.set_up_garden_timing()

    def set_up_garden_timing(self):
        # Create datetime for when the light should first start
        self.grow_light.next_time_on = datetime(2021, self.current_month, self.day_of_month,
                                                self.light_start_time_int // 100, self.light_start_time_int % 100)

        # If the light start time has already passed
        if self.light_start_time_int < self.current_time_int:
            s = self.grow_light.next_time_on
            self.grow_light.next_time_on = s.replace(day=s.day + 1)

        self.grow_light.duration = timedelta(hours=self.light_duration)
        self.grow_light.next_time_off = self.grow_light.next_time_on + self.grow_light.duration

        self.next_feed = self.user_start_datetime + self.feed_duration # TODO: Ask user for last feed time?

    # Set up GPIO mode and pins to IN or OUT
    def setup_pins(self):
        # Pin Setup:
        GPIO.setmode(GPIO.BCM)
        for lcd in self.lcd_pins.values():
            GPIO.setup(lcd.id, GPIO.OUT) # LCD pins set as output
        for led in self.led_pins.values():
            GPIO.setup(led, GPIO.OUT) # LED pins set as output
        for relay in self.relay_pins:
            GPIO.setup(relay, GPIO.OUT)  # relay pins set as output
        for water_sensor in self.water_sensor_pins:
            GPIO.setup(water_sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        return

    def get_current_clock_time(self):
        self.current_pi_time = datetime.now()
        self.current_time = self.current_pi_time + self.clock_difference
        return self.current_time

    # Display message, collect and validate response
    def ask_question(self, question, validate):
        input_valid = False
        input = None
        while not input_valid:
            self.lcd_display.display_text(question)
            
            input_str = self.keypad.receive_input('#', self.lcd_display)
            input_str = input_str.replace('#', '')
            input_str = input_str.replace('*', '')
            
            if input_str != '':
                input = int(input_str)
            else:
                input = 0
            input_valid = validate(input)
            if not input_valid:
                self.lcd_display.display_text('Error with input\nTry again')
                time.sleep(1)

        return input

    # Ask user for input regarding timing
    def request_input(self):

        # Display "Hello Kelsey!" or "Hello Ashley!"
        # TODO

        # User input questions

        # Month must be between 1 and 12
        self.current_month = self.ask_question('Current month?\n', lambda x: (1 <= x) and (x <= 12))

        # Day of month must be between 1 and 31. Shorter months will be dealt with later.
        self.day_of_month = self.ask_question('Day of month?\n', lambda x: (1 <= x) and (x <= 31))

        # Hour must be between 1 and 12, minutes must be less than or equal to 59
        self.current_time_int = self.ask_question('Current time?\n',
                                         lambda x: (1 <= x // 100) and (x // 100 <= 12) and \
                                                   (x % 100 <= 59))

        # Keep track of what time the Pi thinks it is
        self.startup_pi_time = datetime.now()

        # User can choose only 1 or 2
        self.am_or_pm_current = self.ask_question('AM(1) or PM(2)?\n', lambda x: (x==1) or (x==2))

        # Hour must be between 1 and 12, minutes must be less than or equal to 59
        self.light_start_time = self.ask_question('Light starttime?\n',
                                             lambda x: (1 <= x // 100) and (x // 100 <= 12) and \
                                                       (x % 100 <= 59))

        # User can choose only 1 or 2
        self.am_or_pm_light_start = self.ask_question('AM(1) or PM(2)?\n', lambda x: (x==1) or (x==2))

        # Light must be on for at least one hour, no more than 23
        self.light_duration = self.ask_question('Light duration?\n', lambda x: (1 <= x) and (x <= 23))

if __name__ == "__main__":

    garden = Garden()

    try:
        while True:

            # Display current time
            cur_time = self.get_current_clock_time()
            msg = str(cur_time)

            if self.grow_light.is_on == True:
                msg = msg + 'Next light off: ' + str(self.grow_light.next_time_off)
                if cur_time > self.grow_light.next_time_off:
                    self.grow_light.turn_off()
            else:
                msg = msg + 'Next light on: ' + str(self.grow_light.next_time_on)
                if cur_time > self.grow_light.next_time_on:
                    self.grow_light.turn_on()

            # Display current time and next time light turns on/off
            self.lcd_display.display_text(msg)

            # Check if current time > next water level check
            water_too_low = self.water_level_sensor.check_water_level()
            if water_too_low:
                msg = 'ADD WATER'
                self.lcd_display.display_text(msg)

            time.sleep(60)
            # TODO:
            # Check if current time > next feeding
            # Check for keypad entries
    except:
        GPIO.cleanup() # cleanup all GPIO
