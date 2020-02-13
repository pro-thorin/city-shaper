#!/usr/bin/env micropython
from time import sleep
from ev3_robot import Ev3Robot

def trip2():
    #defining
    robot = Ev3Robot()
    robot.read_calibration()
    # solving mission 6, traffic jam
    robot.go_straight_forward(cm = 67.5, speed=35)
    robot.go_straight_forward(cm = 10, speed=40)
    robot.spin_right(degrees = 8)
    sleep(0.1)
    robot.spin_left(degrees = 98)
    robot.go_straight_backward(cm = 10, speed=30)

    robot.align(5)
    robot.go_straight_forward(12, 30)
    robot.spin_right(60)
    robot.go_straight_forward(25, 35)
    robot.align(15)
    robot.go_straight_forward(20, 25)
    robot.spin_right(90)
    robot.go_straight_backward(6, 25)
    robot.align(15)
    robot.go_straight_forward(7, 25)
    robot.spin_left(90)
    robot.go_straight_forward(12, 25)
    # turns to flip elevator
    robot.spin_right(30)
    robot.go_straight_backward(15, 25)
    robot.spin_right(60)
    robot.go_straight_backward(8, 25)
    robot.align(15)
    robot.go_straight_forward(13, 25)
    robot.spin_left(50)
    robot.go_straight_forward(13, 25)
    robot.go_straight_forward(cm=8, speed=5)
    robot.go_straight_backward(2, 25)
    robot.spin_right(25, 20)
    robot.go_straight_backward(5, 25)
    robot.spin_right(20)
    robot.go_straight_backward(5, 25)
    robot.spin_right(50)
    robot.go_straight_forward(11,25)
    robot.spin_left(25)
    robot.go_straight_backward(12, 30)
    robot.spin_left(70)
    robot.go_straight_backward(180, 60)


if __name__ == '__main__':
    trip2()