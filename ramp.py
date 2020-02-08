#!/usr/bin/env micropython
from ev3_robot import Ev3Robot
from time import sleep
robot = Ev3Robot()

robot.go_straight_backward(30, speed=30)
robot.go_straight_backward(15, speed=20)
robot.go_straight_forward(7)
robot.go_straight_backward(20, speed=100)
robot.spin_left(30)
robot.go_straight_backward(120, speed=36)
sleep(1)

while True:
    robot.stop()