#!/usr/bin/env micropython
from ev3dev2.motor import OUTPUT_C, OUTPUT_B, OUTPUT_A, OUTPUT_D, MoveSteering, LargeMotor, MoveTank, MediumMotor
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor
from sys import stderr
from ev3_robot import Ev3Robot

robot = Ev3Robot()
medium_motor = MediumMotor(OUTPUT_D)
medium_motor.on_for_degrees(speed = SpeedDPS(1024), degrees = 100)
robot.go_straight_forward(cm = 10, speed = 30)
