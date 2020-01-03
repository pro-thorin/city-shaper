#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveTank, MoveSteering
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor
from time import sleep
from ev3_robot import Ev3Robot

#Defining
def trip1():
    robot = Ev3Robot()
    #push the lever up to release the blue block
    robot.go_straight_forward(cm=59, speed=-30)
    sleep(1)
    robot.go_straight_backward(cm=18, speed=-30)
    robot.spin_right(degrees= 90, speed=20)
    #go back to home
    robot.go_straight_backward(cm = 65, speed = -70)


if __name__ == '__main__':
    trip1
