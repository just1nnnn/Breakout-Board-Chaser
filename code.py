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
led_7 = digitalio.DigitalInOut(board.GP7)
led_7.direction = digitalio.Direction.OUTPUT
led_8 = digitalio.DigitalInOut(board.GP8)
led_8.direction = digitalio.Direction.OUTPUT
led_9 = digitalio.DigitalInOut(board.GP9)
led_9.direction = digitalio.Direction.OUTPUT
led_10 = digitalio.DigitalInOut(board.GP10)
led_10.direction = digitalio.Direction.OUTPUT
led_11 = digitalio.DigitalInOut(board.GP11)
led_11.direction = digitalio.Direction.OUTPUT
led_12 = digitalio.DigitalInOut(board.GP12)
led_12.direction = digitalio.Direction.OUTPUT
led_13 = digitalio.DigitalInOut(board.GP13)
led_13.direction = digitalio.Direction.OUTPUT
led_14 = digitalio.DigitalInOut(board.GP14)
led_14.direction = digitalio.Direction.OUTPUT
led_15 = digitalio.DigitalInOut(board.GP15)
led_15.direction = digitalio.Direction.OUTPUT
led_16 = digitalio.DigitalInOut(board.GP16)
led_16.direction = digitalio.Direction.OUTPUT
led_17 = digitalio.DigitalInOut(board.GP17)
led_17.direction = digitalio.Direction.OUTPUT
led_18 = digitalio.DigitalInOut(board.GP18)
led_18.direction = digitalio.Direction.OUTPUT
led_19 = digitalio.DigitalInOut(board.GP19)
led_19.direction = digitalio.Direction.OUTPUT
led_20 = digitalio.DigitalInOut(board.GP20)
led_20.direction = digitalio.Direction.OUTPUT
led_21 = digitalio.DigitalInOut(board.GP21)
led_21.direction = digitalio.Direction.OUTPUT
led_22 = digitalio.DigitalInOut(board.GP22)
led_22.direction = digitalio.Direction.OUTPUT
led_26 = digitalio.DigitalInOut(board.GP26)
led_26.direction = digitalio.Direction.OUTPUT
led_27 = digitalio.DigitalInOut(board.GP27)
led_27.direction = digitalio.Direction.OUTPUT
led_28 = digitalio.DigitalInOut(board.GP28)
led_28.direction = digitalio.Direction.OUTPUT

while True:
    led_0.value = True
    time.sleep(0.1)
    led_0.value = False
    led_1.value = True
    time.sleep(0.1)
    led_1.value = False
