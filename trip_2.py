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
    motor1 = LargeMotor(OUTPUT_B)
    motor2 = LargeMotor(OUTPUT_C)
    tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)
    #solving mission 6, traffic jam
    # robot.go_straight_forward(cm = 67.5, speed = -30)
    # robot.go_straight_forward(cm = 10, speed = -40)
    # robot.spin_right(degrees = 4)
    # sleep(1)
    # robot.spin_left(degrees = 94)
    # sleep(1)
    # robot.go_straight_backward(cm = 15, speed = -30)
    # robot.align(5)
    # #solving mission 7, swing
    # robot.spin_right(degrees = 85, speed = 20)
    # sleep(1)
    # robot.go_straight_forward(cm = 50, speed = -20)
    robot.go_straight_backward(cm = 60, speed = -50)

if __name__ == '__main__':
    trip2()