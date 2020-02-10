#!/usr/bin/env micropython
from ev3_robot import Ev3Robot
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from time import sleep
move_steering = MoveSteering(OUTPUT_B, OUTPUT_C)
robot = Ev3Robot()

robot.go_straight_backward(30, speed=30)
robot.go_straight_backward(15, speed=20)
robot.go_straight_forward(7)
robot.go_straight_backward(57, speed=45)
# robot.spin_left(30)
# robot.go_straight_backward(40, speed=40)
# robot.go_straight_backward(40, speed=37.5)
# robot.spin_right(30)
# robot.go_straight_backward(40, speed=35)
# sleep(1)
while True:
    robot.stop()