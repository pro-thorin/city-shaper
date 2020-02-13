#!/usr/bin/env micropython
from time import sleep
from ev3_robot import Ev3Robot

robot = Ev3Robot()
# robot.go_straight_forward(cm = 87)
# robot.dog_gear(degrees = 180, motor = 3, speed = -100)
# robot.spin_left(degrees = 30)
# robot.go_straight_forward(cm = 22)
# robot.align(t = 15, direction = -1)
# robot.go_straight_forward(8)
# robot.spin_right(90)
# robot.go_straight_backward(22)
# robot.go_straight_forward(15)
# robot.go_straight_backward(68, 3, 46)
# robot.dog_gear(degrees = 180, motor = 3, speed = 100)
# while True: 
#     robot.stop()



robot.spin_right(35)
robot.go_straight_forward(65.5)
robot.spin_right(8, 25)
robot.go_straight_backward(3.5)

robot.dog_gear(motor = 4, degrees = 135, speed = -30)
robot.go_straight_forward(2)
robot.spin_left(15)
robot.dog_gear(degrees = 405, motor = 4, speed = 10)
robot.spin_right(29)

robot.go_straight_forward(10, 5)
robot.dog_gear(degrees = 200, motor = 3, speed = -10)

