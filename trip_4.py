#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveTank, MoveSteering
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor
from time import sleep
from ev3_robot import Ev3Robot

def trip4():
    robot = Ev3Robot()
    robot.go_straight_forward(cm = 64, speed = -20)
    robot.go_straight_backward(cm = 10, speed = -50)
    robot.spin_left(degrees = 70)
    robot.go_straight_backward(cm = 18, speed = -40)
    robot.spin_right(degrees = 60)
    robot.go_straight_forward(cm = 35, speed = -45)
    robot.align(15)
    robot.go_straight_forward(cm = 3, speed = -40)
    robot.spin_right(degrees = 80)
    robot.go_straight_backward(cm = 40, speed = -50)
    robot.go_straight_backward(cm = 10, speed = -10)

if __name__ == '__main__':
    trip4()
