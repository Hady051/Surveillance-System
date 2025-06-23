import RPi.GPIO as GPIO
import time

PIR_pin = 12
led_pin = 36

GPIO.setmode(GPIO.BOARD)

GPIO.setup(PIR_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
# pull down resistor inside RPi because floating values might occur
GPIO.setup(led_pin, GPIO.OUT)
GPIO.output(led_pin, 0)

try:
    while True:
        time.sleep(0.01)
        PIR_value = GPIO.input(PIR_pin)
        if PIR_value == 1:
            GPIO.output(led_pin, 1)
        else:
            GPIO.output(led_pin, 0)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('Interrupt worked')