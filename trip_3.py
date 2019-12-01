#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveTank, MoveSteering
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor
from time import sleep
from ev3_robot import Ev3Robot
tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)
#Defining
gyro = GyroSensor()
robot = Ev3Robot()
motor1 = LargeMotor(OUTPUT_B)
motor2 = LargeMotor(OUTPUT_C)
#solving mission 6, traaffic jam
robot.go_straight_forward(cm = 65, speed = -30)
robot.go_straight_forward(cm = 5, speed = -40)
robot.spin_left(degrees = 0.9)
robot.go_straight_forward(cm = 20, speed = -30)
#solving mission 7, swing
robot.pivot_left(degrees = 60, speed = 20)
motor1.off
motor2.off
sleep(1)
robot.go_straight_forward(cm = 10, speed = -20)
robot.pivot_right(degrees = 52, speed = 20)
motor1.off
motor2.off
sleep(1)
robot.go_straight_forward(cm = 20, speed = -20)
robot.go_straight_forward(cm = 30, speed = -30)
robot.go_straight_backward(cm = 20, speed = -30)
robot.spin_left(degrees = 21.9)
motor1.off
motor2.off
sleep(0.5)
robot.go_straight_forward(cm = 48, speed = -30)
