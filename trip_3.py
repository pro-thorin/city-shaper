#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveTank, MoveSteering
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor
from time import sleep
from ev3_robot import Ev3Robot
#aligned at the rig's top right corner at (4, 2.25)
def trip3():
    robot = Ev3Robot()
    robot.go_straight_forward(48)
    robot.go_straight_backward(cm = 10,speed = -20)
    robot.spin_right(90)
    robot.go_straight_backward(cm = 40,speed = -20)

if __name__ == '__main__':
    trip3()