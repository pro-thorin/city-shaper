#!/usr/bin/env micropython
from ev3_robot import Ev3Robot
def trip4(state):
    robot = Ev3Robot()
    robot.go_straight_forward(cm = 66, speed = -20)
    robot.go_straight_backward(cm = 100, speed = -50)