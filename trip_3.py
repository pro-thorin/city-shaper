#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveTank, MoveSteering
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor
from time import sleep
from ev3_robot import Ev3Robot
tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)
gyro = GyroSensor()
robot = Ev3Robot()
robot.go_straight_forward(cm = 46, speed = -30)
robot.go_straight_forward(cm = 5, speed = -40)
robot.spin_left(degrees = 0.9)
robot.go_straight_forward(cm = 20, speed = -30)
robot.pivot_left(degrees = 60, speed = 20)
motor1.off
motor2.off
sleep(1)
robot.pivot_right(degrees = 60, speed = 20)
robot.go_straight_forward(cm = 30, speed = -30)
