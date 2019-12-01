#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveTank, MoveSteering
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor
from time import sleep
from ev3_robot import Ev3Robot

tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)
gyro = GyroSensor()

robot = Ev3Robot()
robot.go_straight_forward(cm = 70, speed = 30)
robot.go_straight_forward(cm = 10, speed = 7.5)
robot.go_straight_forward(cm = -40, speed = 30)
robot.spin_right(degrees = 90, speed = 20)
robot.go_straight_forward(cm = -60, speed = 30)

