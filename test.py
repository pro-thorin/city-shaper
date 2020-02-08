#!/usr/bin/env micropython
from time import sleep
from ev3_robot import Ev3Robot
from ev3dev2.motor import MoveSteering, MoveTank, LargeMotor, OUTPUT_B, OUTPUT_C

steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
robot = Ev3Robot()

robot.go_straight_forward(7)
robot.go_straight_backward(80, 50)
robot.dog_gear(degrees = 180, motor = 3, speed = -100)
while True: 
    robot.stop()


# robot.spin_right(35)
# robot.go_straight_forward(65.5)
# robot.spin_right(8, 25)
# robot.go_straight_backward(3.5)
# robot.dog_gear(motor = 4, degrees = 135, speed = -5)
# robot.go_straight_forward(2)
# robot.spin_left(15)
# robot.dog_gear(degrees = 405, motor = 4, speed = 10)
# robot.spin_right(27.5)
# robot.go_straight_forward(10, 5)
# robot.dog_gear(degrees = 200, motor = 3, speed = -10)

