"""Main module."""

# External module imports
import RPi.GPIO as GPIO
import time
from collapsible_garden import config

class Garden:

    def __init__(self):
        self.lcd_pins = config['lcd_pins']
        self.led_pins = config['led_pins']
        self.keypad_pins = config['keypad_pins']
        self.relay_pins = config['relay_pins']

        # Set up GPIO mode and pins to IN or OUT
        self.setup_pins()

        # Ask for user input upon startup
        self.ask_input()

    # Set up GPIO mode and pins to IN or OUT
    def setup_pins(self):
        # Pin Setup:
        GPIO.setmode(GPIO.BOARD) # Broadcom pin-numbering scheme
        for lcd in self.lcd_pins:
            GPIO.setup(lcd, GPIO.OUT) # LCD pins set as output
        for led in self.led_pins:
            GPIO.setup(led, GPIO.OUT) # LED pins set as output
        for keypad in self.keypad_pins:
            # TODO: pull-up or pull-down?
            GPIO.setup(keypad, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # keypad pins set as input
        for relay in self.relay_pins:
            GPIO.setup(relay, GPIO.OUT)  # relay pins set as output
        return

    # Ask user for input regarding timing
    def ask_input(self):

        # Display "Hello Kelsey!" or "Hello Ashley!"
        # TODO

        # User input questions
        questions = ['Current month?',
                     'Day of month?',
                     'Current time?',
                     'AM(*) or PM(#)?'
                     'Light starttime?',
                     'AM(*) or PM(#)?'
                     'Light duration?']


if __name__ == "__main__":



    while True:
        pass
        # Display current time, next on/off, feeding
        # Check if current time > next light switch
        # Check if current time > next feeding
        # Check if current time > next water level check
        # Check for keypad entries


    try:
        while 1:
            if GPIO.input(butPin): # button is released
                pwm.ChangeDutyCycle(dc)
                GPIO.output(ledPin, GPIO.LOW)
            else: # button is pressed:
                pwm.ChangeDutyCycle(100-dc)
                GPIO.output(ledPin, GPIO.HIGH)
                time.sleep(0.075)
                GPIO.output(ledPin, GPIO.LOW)
                time.sleep(0.075)
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        pwm.stop() # stop PWM
        GPIO.cleanup() # cleanup all GPIO
