"""Main module."""

# External module imports
import RPi.GPIO as GPIO
import time
from collapsible_garden import config

# Set up GPIO mode and pins to IN or OUT
def setup_pins(lcd_pins, led_pins, keypad_pins, relay_pins):

    # Pin Setup:
    GPIO.setmode(GPIO.BOARD) # Broadcom pin-numbering scheme
    for lcd in lcd_pins:
        GPIO.setup(lcd, GPIO.OUT) # LCD pins set as output
    for led in led_pins:
        GPIO.setup(led, GPIO.OUT) # LED pins set as output
    for keypad in keypad_pins:
        # TODO: pull-up or pull-down?
        GPIO.setup(keypad, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # keypad pins set as input
    for relay in relay_pins:
        GPIO.setup(relay, GPIO.OUT)  # relay pins set as output
    return

def ask_input(lcd_pins, keypad_pins):

    questions = ['Current month?',
                 'Day of month?',
                 'Current time?',
                 'AM(1) or PM(2)?'
                 'Light starttime?',
                 'AM(1) or PM(2)?'
                 'Light duration?']


if __name__ == "__main__":

    lcd_pins = config['lcd_pins']
    led_pins = config['led_pins']
    keypad_pins = config['keypad_pins']
    relay_pins = config['relay_pins']

    # Set up GPIO mode and pins to IN or OUT
    setup_pins(lcd_pins, led_pins, keypad_pins, relay_pins)

    # Ask for user input upon startup
    ask_input(lcd_pins, keypad_pins)

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
