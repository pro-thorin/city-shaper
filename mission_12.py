#!/usr/bin/env python3
from ev3_robot import Ev3Robot
move = Ev3Robot()
move.move_in_cm(centimeters = 41, speed = 20)
