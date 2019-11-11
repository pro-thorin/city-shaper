#!/usr/bin/env micropython
from ev3dev2.motor import OUTPUT_C, OUTPUT_B, OUTPUT_A, MoveSteering, LargeMotor, MoveTank, MediumMotor
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor
from sys import stderr

class Ev3Robot:
    def __init__(self, wheel1 = OUTPUT_B, wheel2 = OUTPUT_C):
        self.steer_pair = MoveSteering(wheel1, wheel2)
        self.gyro = GyroSensor()
        self.tank_pair = MoveTank(wheel1, wheel2)
        self.motorB = LargeMotor(OUTPUT_B)
        self.motorC = LargeMotor(OUTPUT_C)

    def pivot_right(self, degrees, speed = 20):
        self.tank_pair.on(left_speed = 0, right_speed = speed)
        self.gyro.wait_until_angle_changed_by(degrees - 10)
        self.tank_pair.off()
    
    def pivot_left(self, degrees, speed = 20):
        self.tank_pair.on(left_speed = speed, right_speed = 0)
        self.gyro.wait_until_angle_changed_by(degrees - 10)
        self.tank_pair.off()
    
    def spin_right(self, degrees, speed = 20):
        self.gyro.mode = 'GYRO-ANG'
        value1 = self.gyro.angle
        self.tank_pair.on(left_speed = speed, right_speed = speed * -1)
        self.gyro.wait_until_angle_changed_by(degrees)
        self.tank_pair.off()
        value2 = self.gyro.angle
        self.tank_pair.on(left_speed = -20, right_speed = 20)
        self.gyro.wait_until_angle_changed_by(value2 - value1 - degrees)
    
    def spin_left(self, degrees, speed = 20):
        self.gyro.mode = 'GYRO-ANG'
        value1 = self.gyro.angles
        self.gyro.reset()
        self.tank_pair.on(left_speed = speed * -1, right_speed = speed)
        self.gyro.wait_until_angle_changed_by(degrees)
        self.tank_pair.off()
        value2 = self.gyro.angle
        self.tank_pair.on(left_speed = 20, right_speed = -20)
        self.gyro.wait_until_angle_changed_by(value2 - value1 - degrees)

    def go_straight_forward(self, cm, speed = 30):
        value1 = self.motorB.position
        angle0 = self.gyro.angle
        rotations = cm / 19.05
        while (self.motorB.position - value1) / 360 < rotations:
            self.gyro.mode = 'GYRO-ANG'
            angle = self.gyro.angle - angle0
            print(angle, file = stderr)
            self.steer_pair.on(steering = angle * -1, speed = speed)