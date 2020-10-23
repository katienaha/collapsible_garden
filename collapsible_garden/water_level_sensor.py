
# External module imports
import RPi.GPIO as GPIO

# Sensor that checks whether water levels have gone too low
class WaterLevelSensor:

    # Store which pin receives info from the water level sensor
    def __init__(self, pin):
        self.pin = pin
        self.is_too_low = False

    # Check to see if the water level is too low
    def check_water_level(self):

        if GPIO.input(self.pin) == GPIO.HIGH:
            self.is_too_low = True
        else:
            self.is_too_low = False
        return self.is_too_low



