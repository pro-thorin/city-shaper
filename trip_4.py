#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveTank, MoveSteering
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor
from time import sleep
from ev3_robot import Ev3Robot

def trip4():
    robot = Ev3Robot()
    robot.go_straight_forward(cm = 66, speed = -20)
    robot.go_straight_backward(cm = 10, speed = -50)
    robot.spin_left(degrees = 70)
    robot.go_straight_backward(cm = 25, speed = -40)
    robot.align(15)
    robot.spin_right(degrees = 90)
    robot.go_straight_forward(cm = 50, speed = -40)
    robot.spin_right(degrees = 51.1)
    robot.go_straight_backward(cm = 80, speed = -70)

if __name__ == '__main__':
    trip4()
