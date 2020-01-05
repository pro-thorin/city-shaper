#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveTank, MoveSteering
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor
from time import sleep
from ev3_robot import Ev3Robot
 
def trip4():
    robot = Ev3Robot()
    #push innovative architecture, sustainability upgrade, and red block
    robot.go_straight_forward(cm = 64, speed=20)
    robot.go_straight_backward(cm = 10, speed=50)
    robot.spin_left(degrees = 82)
    robot.go_straight_backward(cm = 18, speed=40)
    robot.spin_right(degrees = 75)
    robot.go_straight_forward(cm = 35, speed=45)
    robot.align(15)
    robot.go_straight_forward(cm = 4, speed=20)
    robot.spin_right(degrees = 90)
    #try and go backwards onto the bridge
    robot.go_straight_backward(45, speed=30)
    robot.go_straight_forward(7)
    robot.go_straight_backward(32.5, speed=45)
    while 1 == 1:
        robot.stop()

if __name__ == '__main__':
    trip4()
