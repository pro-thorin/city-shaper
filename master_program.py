#!/usr/bin/env micropython
from ev3dev2.button import Button
from time import sleep
from trip_1 import trip1
from trip_2 import trip2
from trip_3 import trip3
from trip_4 import trip4

btn = Button()
btn._state = set()

def left(state):
    trip1()
    btn._state = set()
def right(state):
    trip2()
    btn._state = set()
def up(state):
    trip3()
    btn._state = set()
def down(state):
    trip4()
    btn._state = set()

# Do something when state of any button changes:

btn.on_left = left
btn.on_right = right
btn.on_up = up
btn.on_down = down

while True:
    btn.process()
    sleep(0.01)
    