import time
import board
import digitalio

led_0 = digitalio.DigitalInOut(board.GP0)
led_0.direction = digitalio.Direction.OUTPUT
led_1 = digitalio.DigitalInOut(board.GP1)
led_1.direction = digitalio.Direction.OUTPUT
led_2 = digitalio.DigitalInOut(board.GP2)
led_2.direction = digitalio.Direction.OUTPUT
led_3 = digitalio.DigitalInOut(board.GP3)
led_3.direction = digitalio.Direction.OUTPUT
led_4 = digitalio.DigitalInOut(board.GP4)
led_4.direction = digitalio.Direction.OUTPUT
led_5 = digitalio.DigitalInOut(board.GP5)
led_5.direction = digitalio.Direction.OUTPUT
led_6 = digitalio.DigitalInOut(board.GP6)
led_6.direction = digitalio.Direction.OUTPUT

while True:
    led_0.value = True
    time.sleep(0.1)
    led_0.value = False
    led_1.value = True
    time.sleep(0.1)
    led_1.value = False
    led_2.value = True
    time.sleep(0.1)
    led_2.value = False
    led_3.value = True
    time.sleep(0.1)
    led_3.value = False
    led_4.value = True
    time.sleep(0.1)
    led_4.value = False
    led_5.value = True
    time.sleep(0.1)
    led_5.value = False
    led_6.value = True
    time.sleep(0.1)
    led_6.value = False

