#!/usr/bin/env micropython
from ev3_robot import Ev3Robot
robot = Ev3Robot()
robot.go_straight_forward(centimeters = 41, speed = 20)
