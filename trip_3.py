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
robot.read_calibration()
motor1 = LargeMotor(OUTPUT_B)
motor2 = LargeMotor(OUTPUT_C)
#solving mission 6, traaffic jam
robot.go_straight_forward(cm = 67.5, speed = -30)
robot.go_straight_forward(cm = 10, speed = -40)
robot.spin_right(degrees = 4)
robot.spin_left(degrees = 94)
robot.go_straight_forward(cm = 5, speed = -10)
robot.go_straight_backward(cm = 15, speed = -30)
robot.align(5)
#solving mission 7, swing
robot.spin_right(degrees = 90, speed = 20)
robot.go_straight_forward(cm = 50, speed = -20)
robot.spin_right(degrees = 10)
robot.go_straight_backward(cm = 1000000, speed = -50)
# robot.pivot_right(degrees = 56, speed = 20)
# motor1.off
# motor2.off

# sleep(1)
# robot.go_straight_forward(cm = 50, speed = -20)
# robot.go_straight_backward(cm = 20, speed = -30)
# robot.pivot_left(degrees = 25)
# motor1.off
# motor2.off
# sleep(1)
# robot.go_straight_forward(cm = 48, speed = -30)
# robot.spin_right(degrees = 90)