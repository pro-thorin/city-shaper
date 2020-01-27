#!/usr/bin/env micropython
from ev3_robot import Ev3Robot
from time import sleep
robot = Ev3Robot()

robot.turn(steering=100, degrees=90)
sleep(5)
robot.turn(steering=100, degrees=180)
