#!/usr/bin/env micropython
from ev3_robot import Ev3Robot
#aligned at the rig's top right corner at (4, 2.25)
def trip3():
    robot = Ev3Robot()
    #push all 13 blocks into the black circle
    robot.go_straight_forward(47.5)
    robot.go_straight_backward(cm = 10,speed=20)
    robot.spin_right(90)
    #go back to home today
    robot.go_straight_backward(cm = 40,speed=40)

if __name__ == '__main__':
    trip3()