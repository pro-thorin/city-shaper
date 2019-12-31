#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveTank, MoveSteering
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor
from time import sleep
from ev3_robot import Ev3Robot
from ev3dev2.button import Button
from sys import stderr

#Defining

tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)
gyro = GyroSensor()
robot = Ev3Robot()
motor1 = LargeMotor(OUTPUT_B)
motor2 = LargeMotor(OUTPUT_C)
button = Button()

while not button.any():
    sleep(0.01)

#Solving mission 12 and 2 (12 = Design and Build, 2 = Crane)
# robot.go_straight_forward(cm = 58, speed = -30)
# robot.go_straight_forward(cm = 16, speed = -7.5)
# robot.go_straight_backward(cm = 30, speed = -30)
# robot.spin_right(degrees = 70, speed = 20)
# motor1.off()
# motor2.off()
# sleep(1)
# robot.go_straight_backward(cm = 20, speed = -30)
# sleep(2)
print("Bob is cool!", file = stderr)
sleep(5)
print("HEIEIE", file = stderr)

while not button.any():
    sleep(0.01)

# #solving mission 6, traffic jam
# robot.go_straight_forward(cm = 67.5, speed = -30)
# robot.go_straight_forward(cm = 10, speed = -40)
# robot.spin_right(degrees = 4)
# robot.spin_left(degrees = 94)
# robot.go_straight_forward(cm = 5, speed = -10)
# robot.go_straight_backward(cm = 15, speed = -30)
# robot.align(5)

# #solving mission 7, swing
# robot.spin_right(degrees = 90, speed = 20)
# robot.go_straight_forward(cm = 50, speed = -20)
# robot.spin_right(degrees = 7)
# robot.go_straight_backward(cm = 1000, speed = -50)
sleep(5)

while not button.any():
    sleep(0.01)

# #solving mission 11 & 12, innovative architecture/design and build
# robot.go_straight_forward(cm = 66, speed = -20)
# robot.go_straight_backward(cm = 100, speed = -50)
