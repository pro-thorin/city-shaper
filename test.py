#!/usr/bin/env micropython
from ev3_robot import Ev3Robot
robot = Ev3Robot()

robot.go_straight_backward(30, -30)
robot.go_straight_forward(7)
robot.go_straight_backward(34, -45)
while 1 == 1:
    robot.stop()
