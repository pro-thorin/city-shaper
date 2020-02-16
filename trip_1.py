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
    robot.go_straight_forward(9, 15)
    robot.dog_gear(degrees = 250, motor = 3, speed = -10)
    # raises the lever on the crane, releasing the blue block 
    robot.go_straight_backward(39, speed = 30)
    robot.spin_left(75)
    robot.go_straight_forward(26)
    robot.go_straight_forward(1, 5)
    robot.go_straight_backward(12)
    robot.spin_right(60, speed = 40)
    robot.go_straight_backward(70, speed = 55)
if __name__ == '__main__':
    trip1()
