#!/usr/bin/env micropython
from ev3_robot import Ev3Robot
 
def trip4():
    robot = Ev3Robot()
    # push innovative architecture, sustainability upgrade, and red block
    robot.go_straight_forward(cm = 87)
    robot.dog_gear(degrees = 180, motor = 3, speed = -100)
    robot.spin_left(degrees = 30)
    robot.go_straight_forward(cm = 22)
    robot.align(t = 15, direction = -1)
    robot.go_straight_forward(8)
    robot.spin_right(90)
    robot.go_straight_backward(22)
    robot.go_straight_forward(15)
    robot.go_straight_backward(70, 55, 3)
    robot.dog_gear(degrees = 180, motor = 3, speed = 100)
    while True: 
        robot.stop()


if __name__ == '__main__':
    trip4()
