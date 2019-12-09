#!/usr/bin/env micropython
from ev3dev2.motor import OUTPUT_C, OUTPUT_B, OUTPUT_A, OUTPUT_D, MoveSteering, LargeMotor, MoveTank, MediumMotor
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor
from sys import stderr
from ev3_robot import Ev3Robot

robot = Ev3Robot()
robot.read_calibration()
tank_pair = MoveTank(OUTPUT_C, OUTPUT_B)
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
medium_motorA = MediumMotor(OUTPUT_A)
medium_motorD = MediumMotor(OUTPUT_D)

# Mission 4
medium_motorA.on_for_degrees(degrees = 135, speed = -30)
robot.go_straight_forward(76)
medium_motorD.on_for_degrees(degrees = 360, speed = -100)
robot.spin_right(5)
robot.go_straight_backward(cm = 4, speed = -20)
medium_motorA.on_for_degrees(degrees = 135, speed = 30)
