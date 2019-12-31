#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveTank, MoveSteering
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor
from time import sleep
from ev3_robot import Ev3Robot
<<<<<<< HEAD

tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)
gyro = GyroSensor()
robot = Ev3Robot()
motor1 = LargeMotor(OUTPUT_B)
motor2 = LargeMotor(OUTPUT_C)

robot.go_straight_forward(48)
robot.go_straight_backward(cm = 10,speed = -20)
robot.spin_right(90)
robot.go_straight_backward(cm = 20,speed = -20)
   
=======
def trip3(state):
    robot = Ev3Robot()
    robot.go_straight_forward(48)
    robot.go_straight_backward(cm = 10,speed = -20)
    robot.spin_right(90)
    robot.go_straight_backward(cm = 20,speed = -20)
>>>>>>> f43be81697edd944d4136a0ca48196c8e886b76e
