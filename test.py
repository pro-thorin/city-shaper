#!/usr/bin/env micropython
from ev3dev2.motor import OUTPUT_C, OUTPUT_B, OUTPUT_A, OUTPUT_D, MoveSteering, LargeMotor, MoveTank, MediumMotor
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor, ColorSensor
from sys import stderr
from ev3_robot import Ev3Robot
from ev3dev2.button import Button

robot = Ev3Robot()
tank_pair = MoveTank(OUTPUT_C, OUTPUT_B)
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
medium_motorA = MediumMotor(OUTPUT_A)
medium_motorD = MediumMotor(OUTPUT_D)
button = Button()

# robot.spin_left(degrees = 90, speed = 15)

robot.go_straight_backward(cm = 40, speed = -100)