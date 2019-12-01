#!/usr/bin/env micropython
from ev3dev2.motor import OUTPUT_C, OUTPUT_B, OUTPUT_A, OUTPUT_D, MoveSteering, LargeMotor, MoveTank, MediumMotor
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor
from sys import stderr
from ev3_robot import Ev3Robot

robot = Ev3Robot()
tank_pair = MoveTank(OUTPUT_C, OUTPUT_B)
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
medium_motorA = MediumMotor(OUTPUT_A)
medium_motorD = MediumMotor(OUTPUT_D)

medium_motorD.on_for_degrees(degrees = 90, speed = 30)
robot.go_straight_forward(cm = 45.72, speed = SpeedDPS(-512))
robot.spin_right(degrees = 43)
robot.go_straight_forward(cm = 53.34)

robot.go_straight_backward(cm = 70)
robot.spin_right(degrees = 50)
robot.go_straight_forward(cm = 91.44)
robot.spin_left(degrees = 30)
robot.go_straight_forward(cm = 12.5)


