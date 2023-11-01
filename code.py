import time
import board
import digitalio
import pwmio

from adafruit_motor import motor #Imports a function from the adafruit_motor library

right_motor_forward = board.GP1 # Initializes the variable left_motor_forward and attaches it to GP12
right_motor_backward = board.GP2 #Initializes the variable left_motor_backward and attaches it to GP13
left_motor_forward = board.GP12
left_motor_backward = board.GP13

pwm_Ra = pwmio.PWMOut(right_motor_forward, frequency=10000) #Tells the controller that the motor is an input
pwm_Rb = pwmio.PWMOut(right_motor_backward, frequency=10000) #Tells the controller that the motor is an output
pwm_La = pwmio.PWMOut(left_motor_forward, frequency=10000)
pwm_Lb = pwmio.PWMOut(left_motor_backward, frequency=10000)

Right_Motor = motor.DCMotor(pwm_Ra, pwm_Rb) #Configuration line (it is required)
Right_Motor_speed = 0 #Initializes the variable left_motor_forward and starts it at 0
Left_Motor = motor.DCMotor(pwm_La, pwm_Lb)
Left_Motor_speed = 0

def forward():
    Right_Motor_speed = .5
    Right_Motor.throttle = Right_Motor_speed
    Left_Motor_speed = .5
    Left_Motor.throttle = Left_Motor_speed

def backward():
    Right_Motor_speed = -.5
    Right_Motor.throttle = Right_Motor_speed
    Left_Motor_speed = -.5
    Left_Motor.throttle = Left_Motor_speed

def left():
    Right_Motor_speed = .5
    Right_Motor.throttle = Right_Motor_speed
    Left_Motor_speed = 0
    Left_Motor.throttle = Left_Motor_speed

def right():
    Right_Motor_speed = 0
    Right_Motor.throttle = Right_Motor_speed
    Left_Motor_speed = .5
    Left_Motor.throttle = Left_Motor_speed

def stop():
    Right_Motor_speed = 0
    Right_Motor.throttle = Right_Motor_speed
    Left_Motor_speed = 0
    Left_Motor.throttle = Left_Motor_speed

while True:

    forward()
    time.sleep(3)

    stop()
    time.sleep(0.5)

    left()
    time.sleep(1)

    forward()
    time.sleep(2)

    left()
    time.sleep(1)

    forward()
    time.sleep(1)

    left()
    time.sleep(1)
