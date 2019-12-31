#!/usr/bin/env micropython
from ev3_robot import Ev3Robot
def trip4():
    robot = Ev3Robot()
    robot.go_straight_forward(cm = 66, speed = -20)
    robot.go_straight_backward(cm = 100, speed = -50)

if __name__ == '__main__':
    trip4()