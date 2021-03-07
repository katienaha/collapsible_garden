
# External module imports
import RPi.GPIO as GPIO
from datetime import timedelta

# Lightbulb that provides main source of light for plants
class GrowLight:

    # Store which pin is used to control the grow light
    def __init__(self, pin):
        self.pin = pin
        self.is_on = False
        self.duration = timedelta(hours=16)
        self.next_time_on = None
        self.next_time_off = None

    # Turn on the light
    def turn_on(self):
        GPIO.output(self.pin, GPIO.HIGH)
        self.is_on = True

        # Update next time on to be the next day
        on = self.next_time_on
        self.next_time_on = on.replace(days=on.days + 1)

    # Turn off the light
    def turn_off(self):
        GPIO.output(self.pin, GPIO.LOW)
        self.is_on = False

        # Update next time off to be the next day
        off = self.next_time_off
        self.next_time_off = off.replace(days=off.days + 1)


