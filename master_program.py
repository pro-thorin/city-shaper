#!/usr/bin/env micropython
from ev3dev2.motor import OUTPUT_C, OUTPUT_B, OUTPUT_A, OUTPUT_D, MoveSteering, LargeMotor, MoveTank, MediumMotor
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor, ColorSensor
from sys import stderr
from ev3_robot import Ev3Robot
from ev3dev2.button import Button
from time import sleep
from trip_1 import trip1
from trip_2 import trip2
from trip_3 import trip3
from trip_4 import trip4

robot = Ev3Robot()
btn = Button()
btn._state = set()

def left(state):
    trip1()
    btn._state = set()

# Do something when state of any button changes:

btn.on_left = left
btn.on_right = trip2
btn.on_up = trip3
btn.on_down = trip4

<<<<<<< HEAD
# #solving mission 7, swing
# robot.spin_right(degrees = 90, speed = 20)
# robot.go_straight_forward(cm = 50, speed = -20)
# robot.spin_right(degrees = 7)
# robot.go_straight_backward(cm = 1000, speed = -50)
sleep(5)

while not button.any():
=======
while True:
    btn.process()
>>>>>>> f43be81697edd944d4136a0ca48196c8e886b76e
    sleep(0.01)
    