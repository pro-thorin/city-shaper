#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveTank, MoveSteering
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor
from time import sleep
from ev3_robot import Ev3Robot

#Defining
def trip1():
    robot = Ev3Robot()
    robot.go_straight_forward(cm=58, speed=-30)
    robot.go_straight_backward(cm=30, speed=-30)
    robot.spin_right(degrees= 70, speed=20)
    motor1.off()
    motor2.off()
    sleep(1)

trip1()