#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_C, OUTPUT_B, OUTPUT_A, MoveSteering, LargeMotor, MoveTank, MediumMotor
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM

class Ev3Robot:
    def __init__(self, wheel1 = OUTPUT_B, wheel2 = OUTPUT_C):
        self.steer_pair = MoveSteering(wheel1, wheel2)

    def move_in_cm(self, centimeters, speed=SpeedDPS(256)):
        rotations = centimeters / -19.05
        self.steer_pair.on_for_rotations(steering = 0, speed = SpeedDPS(256), rotations = rotations)