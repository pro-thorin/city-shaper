#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveTank, MoveSteering
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor
from time import sleep
from ev3_robot import Ev3Robot

def trip2():
    #defining
    robot = Ev3Robot()
    robot.read_calibration()
    #solving mission 6, traffic jam
    robot.go_straight_forward(cm = 67.5, speed=30)
    robot.go_straight_forward(cm = 10, speed=40)
    robot.spin_right(degrees = 10)
    sleep(0.1)
    robot.spin_left(degrees = 100)
    robot.go_straight_backward(cm = 10, speed=30)

    robot.align(5)
    #solving mission 7, swing
    robot.spin_right(degrees = 95, speed = 20)
    robot.go_straight_forward(cm = 53)
    robot.go_straight_forward(cm = 5, speed=10)
    # solving mission 8 & 9, elevator and safety factor
    robot.go_straight_backward(cm=17)
    robot.spin_left(90)
    robot.go_straight_backward(cm=15, speed=15)
    robot.go_straight_forward(36)
    robot.spin_right(65)
    robot.go_straight_forward(33)
    robot.spin_right(30)
    robot.go_straight_backward(15)
    robot.spin_right(60)
    robot.go_straight_backward(10)
    robot.align(15)
    robot.go_straight_forward(13)
    robot.spin_left(50)
    robot.go_straight_forward(10)
    robot.go_straight_forward(cm=10, speed=5)
    robot.go_straight_backward(2)
    robot.spin_right(22)
    robot.go_straight_backward(5)
    robot.spin_right(30, speed=25)
    robot.go_straight_backward(16)
    robot.spin_left(45)
    robot.go_straight_backward(20)
    robot.spin_left(32)
    robot.go_straight_backward(175, speed=60)

if __name__ == '__main__':
    trip2()