#!/usr/bin/env micropython
from time import sleep
from ev3_robot import Ev3Robot

#Defining
def trip1():
    robot = Ev3Robot()
    #push the lever up to release the blue block
    robot.go_straight_forward(cm=17, speed=30)
    sleep(1)
    robot.spin_right(46)
    robot.go_straight_forward(cm = 55)
    robot.align(15)
    robot.go_straight_forward(cm = 7)
    robot.spin_right(degrees = 15)

    robot.dog_gear(degrees = 180, speed = 50)
    # robot.go_straight_backward(cm=18, speed=30)
    # robot.spin_right(degrees= 90, speed=20)
    # #go back to home
    # robot.go_straight_backward(cm = 65, speed=70)


if __name__ == '__main__':
    trip1
