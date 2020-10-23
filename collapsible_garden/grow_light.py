
# External module imports
import RPi.GPIO as GPIO

# Lightbulb that provides main source of light for plants
class GrowLight:

    # Store which pin is used to control the grow light
    def __init__(self, pin):
        self.pin = pin

    # Turn on the light
    def turn_on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    # Turn off the light
    def turn_off(self):
        GPIO.output(self.pin, GPIO.LOW)


