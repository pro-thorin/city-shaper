#!/usr/bin/env micropython
from time import sleep
from ev3_robot import Ev3Robot

robot = Ev3Robot()

robot.go_straight_forward(cm = 87)
robot.dog_gear(degrees = 180, motor = 3, speed = -100)
robot.spin_left(degrees = 30)
robot.go_straight_forward(cm = 22)
