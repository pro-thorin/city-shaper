#!/usr/bin/env micropython
from ev3_robot import Ev3Robot
from ev3dev2.button import Button
from time import sleep
robot = Ev3Robot()
btn = Button()
btn._state = set()
def left(state):
    if state:
        robot.motor3.on(speed = -10)
    else:
        robot.motor3.off()
        btn._state = set()
def right(state):
    if state:
        robot.motor3.on(speed = 10)
    else:
        robot.motor3.off()
        btn._state = set()
def up(state):
    if state:
        robot.motor4.on(speed = -10)
    else:
        robot.motor4.off()
        btn._state = set()
def down(state):
    if state:
        robot.motor4.on(speed = 10)
    else:
        robot.motor4.off()
        btn._state = set()
    
btn.on_left = left
btn.on_right = right
btn.on_up = up
btn.on_down = down

while True:
    btn.process()
    sleep(0.01)