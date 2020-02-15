#!/usr/bin/env micropython
from time import sleep
from ev3_robot import Ev3Robot

#Defining
def trip1():
    # hangs the bat on the tree
    robot = Ev3Robot()
    robot.spin_right(35)
    robot.go_straight_forward(65.5)
    robot.spin_right(8, 25)
    robot.go_straight_backward(3.5)
    # deposits the blue block into the treehouse
    robot.dog_gear(motor = 4, degrees = 135, speed = -30)
    robot.go_straight_forward(2)
    robot.spin_left(15)
    robot.dog_gear(degrees = 405, motor = 4, speed = 40)
    robot.spin_right(29)
    robot.go_straight_forward(9, 5)
    robot.dog_gear(degrees = 250, motor = 3, speed = -10)
    # raises the lever on the crane, releasing the blue block 
    robot.go_straight_backward(43)
    robot.spin_left(64)
    robot.go_straight_forward(27)
    sleep(1)
    robot.go_straight_backward(3)
    robot.pivot_right(degrees = 65)
    robot.go_straight_backward(10)
    robot.spin_left(50)
    robot.go_straight_forward(27)
    robot.spin_left(90)
    robot.go_straight_forward(27)

if __name__ == '__main__':
    trip1()
