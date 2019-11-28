#!/usr/bin/env micropython
from ev3dev2.motor import OUTPUT_C, OUTPUT_B, OUTPUT_A, MoveSteering, LargeMotor, MoveTank, MediumMotor
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor, ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_4
from sys import stderr
from time import sleep

class Ev3Robot:
    def __init__(self, wheel1 = OUTPUT_B, wheel2 = OUTPUT_C):
        self.steer_pair = MoveSteering(wheel1, wheel2)
        self.gyro = GyroSensor()
        self.tank_pair = MoveTank(wheel1, wheel2)
        self.motor1 = LargeMotor(wheel1)
        self.motor2 = LargeMotor(wheel2)
        self.color1 = ColorSensor(INPUT_1)
        self.color4 = ColorSensor(INPUT_4)

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
        self.tank_pair.on(left_speed = speed * -1, right_speed = speed)
        self.gyro.wait_until_angle_changed_by(degrees)
        self.tank_pair.off()
        value2 = self.gyro.angle
        self.tank_pair.on(left_speed = 20, right_speed = -20)
        self.gyro.wait_until_angle_changed_by(value2 - value1 - degrees)

    def go_straight_forward(self, cm, speed = 30):
        value1 = self.motor1.position
        angle0 = self.gyro.angle
        rotations = cm / 19.05
        while (self.motor1.position - value1) / 360 < rotations:
            self.gyro.mode = 'GYRO-ANG'
            angle = self.gyro.angle - angle0
            self.steer_pair.on(steering = angle * -1, speed = speed)

    def go_straight_backward(self, cm, speed = 30):
        value1 = self.motor1.position
        angle0 = self.gyro.angle
        rotations = cm / 19.05
        while (self.motor1.position - value1) / 360 < rotations:
            self.gyro.mode = 'GYRO-ANG'
            angle = self.gyro.angle - angle0
            self.steer_pair.on(steering = angle, speed = speed * -1)
    
    def calibrate(self):
        print("black")
        sleep(20)
        black1 = self.color1.reflected_light_intensity
        black4 = self.color4.reflected_light_intensity
        print(black1, black4, file = stderr)
        sleep(3)
        print("white")
        sleep(20)
        white1 = self.color1.reflected_light_intensity
        white4 = self.color4.reflected_light_intensity
        print(white1, white4, file = stderr)
        sleep(3)
        self.write_color("black1", black1)
        self.write_color("black4", black4)
        self.write_color("white1", white1)
        self.write_color("white4", white4)

    def write_color(self, file, value):
        f = open(file, "w")
        f.write(value)
        f.close()
    
    def read_color(self, file):
        f = open(file, "r")
        color = f.readline()
        f.close()
        return color

    def align_white(self, speed = 20):
        while self.color1.reflected_light_intensity < 95 and self.color4.reflected_light_intensity < 95:
            self.steer_pair.on(steering = 0, speed = speed)
        self.steer_pair.off()
        if self.color4.reflected_light_intensity > 95:
            while self.color1.reflected_light_intensity < 95:
                self.motor1.on(speed = speed)
            self.motor1.off()
        else: 
            while self.color4.reflected_light_intensity < 95:
                self.motor2.on(speed = speed)
            self.motor2.off()
        print(self.color1.reflected_light_intensity, self.color4.reflected_light_intensity, file = stderr)
    def align_black(self, speed = 20):
        while self.color1.reflected_light_intensity > 16 and self.color4.reflected_light_intensity > 16:
            self.steer_pair.on(steering = 0, speed = speed)
        self.steer_pair.off()
        if self.color4.reflected_light_intensity < 16:
            while self.color1.reflected_light_intensity > 16:
                self.motor1.on(speed = speed)
            self.motor1.off()
        else: 
            while self.color4.reflected_light_intensity > 16:
                self.motor2.on(speed = speed)
            self.motor2.off()
        print(self.color1.reflected_light_intensity, self.color4.reflected_light_intensity, file = stderr)
    def align(self, speed = 20):
        self.align_white(speed)
        self.align_black(-5)
        self.align_white(-5)