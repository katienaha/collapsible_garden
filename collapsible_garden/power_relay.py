
# External module imports
import RPi.GPIO as GPIO

# Power with relay switch to control power to grow light and air pump
class PowerRelay:

    # Store which pin is used to control the relay
    def __init__(self, pin):
        self.pin = pin
        self.is_on = False

    # Turn the "normally off" outlets ON. Note, this will turn the "normally on" outlet OFF.
    def turn_on(self):
        GPIO.output(self.pin, GPIO.HIGH)
        self.is_on = True

    # Turn the "normally off" outlets OFF. Note, this will turn the "normally on" outlet ON.
    def turn_off(self):
        GPIO.output(self.pin, GPIO.LOW)
        self.is_on = False

