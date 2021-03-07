
# External module imports
import RPi.GPIO as GPIO

# LED status light that alerts user when water or food needs to be added
class LedLight:

    def __init__(self, pin):
        self.pin = pin

    def turn_on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def turn_off(self):
        GPIO.output(self.pin, GPIO.LOW)


