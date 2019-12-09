#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveTank, MoveSteering
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor
from time import sleep
from ev3_robot import Ev3Robot
tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)
#Defining
#gyro = GyroSensor()
robot = Ev3Robot()
#robot.read_calibration()
motor1 = LargeMotor(OUTPUT_B)
motor2 = LargeMotor(OUTPUT_C)
robot.go_straight_forward(cm = 47, speed = -30)
robot.go_straight_backward(cm = 10, speed = -50)
robot.spin_right(degrees = 45)
robot.go_straight_backward(cm = 45, speed = -45)