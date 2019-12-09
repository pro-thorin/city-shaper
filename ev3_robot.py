#!/usr/bin/env micropython
from ev3dev2.motor import OUTPUT_C, OUTPUT_B, OUTPUT_A, MoveSteering, LargeMotor, MoveTank, MediumMotor
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor, ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_4
from sys import stderr
from time import sleep

class Ev3Robot:

    __slots__ = [
        '_black1' ,
        '_black4' ,
        '_white1' ,
        '_white4' 

    ]
    def __init__(self, wheel1 = OUTPUT_B, wheel2 = OUTPUT_C):
        self.steer_pair = MoveSteering(wheel1, wheel2)
        self.gyro = GyroSensor()
        self.tank_pair = MoveTank(wheel1, wheel2)
        self.motor1 = LargeMotor(wheel1)
        self.motor2 = LargeMotor(wheel2)
        self.color1 = ColorSensor(INPUT_1)
        self.color4 = ColorSensor(INPUT_4)
        self._black1 = 0
        self._black4 = 0 
        self._white1 = 100
        self._white4 = 100

    def write_color(self, file, value):
        f = open(file, "w")
        f.write(str(value))
        f.close()
    
    def read_color(self, file):
        f = open(file, "r")
        color = int(f.readline().strip())
        f.close()
        return color

    def pivot_right(self, degrees, speed = 20):
        self.tank_pair.on(left_speed = speed, right_speed = 0)
        self.gyro.wait_until_angle_changed_by(degrees - 10)
        self.tank_pair.off()
    
    def pivot_left(self, degrees, speed = 20):
        self.tank_pair.on(left_speed = 0, right_speed = speed)
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
        value1 = self.gyro.angle
        self.tank_pair.on(left_speed = speed * -1, right_speed = speed)
        self.gyro.wait_until_angle_changed_by(degrees)
        self.tank_pair.off()
        value2 = self.gyro.angle
        self.tank_pair.on(left_speed = 20, right_speed = -20)
        self.gyro.wait_until_angle_changed_by(value2 - value1 - degrees)

    def go_straight_forward(self, cm, speed = -20):
        value1 = self.motor1.position
        angle0 = self.gyro.angle
        rotations = cm / 19.05
        while abs(self.motor1.position - value1) / 360 < rotations:
            self.gyro.mode = 'GYRO-ANG'
            angle = self.gyro.angle - angle0
            self.steer_pair.on(steering = angle * -1, speed = speed)

    def go_straight_backward(self, cm, speed = 30):
        value1 = self.motor1.position
        angle0 = self.gyro.angle
        rotations = cm / 19.05
        while abs(self.motor1.position - value1) / 360 < rotations:
            self.gyro.mode = 'GYRO-ANG'
            angle = self.gyro.angle - angle0
            self.steer_pair.on(steering = angle, speed = speed * -1)
    
    def calibrate(self):
        print("black", file = stderr)
        sleep(10)
        self._black1 = self.color1.reflected_light_intensity
        self._black4 = self.color4.reflected_light_intensity
        print(self._black1, self._black4, file = stderr)
        sleep(3)
        print("white", file = stderr)
        sleep(10)
        self._white1 = self.color1.reflected_light_intensity
        self._white4 = self.color4.reflected_light_intensity
        print(self._white1, self._white4, file = stderr)
        sleep(3)
        self.write_color("/tmp/black1", self._black1)
        self.write_color("/tmp/black4", self._black4)
        self.write_color("/tmp/white1", self._white1)
        self.write_color("/tmp/white4", self._white4)
    
    def read_calibration(self):
        self._black1 = self.read_color("/tmp/black1")
        self._black4 = self.read_color("/tmp/black4")
        self._white1 = self.read_color("/tmp/white1")
        self._white4 = self.read_color("/tmp/white4")

    def align_white(self, speed = 20, t = 96.8):
        print(self.calibrate_RLI(self.color1), self.calibrate_RLI(self.color4), file = stderr)
        while self.calibrate_RLI(self.color1) < t and self.calibrate_RLI(self.color4) < t:
            self.steer_pair.on(steering = 0, speed = speed)
        print(self.calibrate_RLI(self.color1), self.calibrate_RLI(self.color4), file = stderr)
        self.steer_pair.off()
        if self.calibrate_RLI(self.color4) > t:
            while self.calibrate_RLI(self.color1) < t:
                self.motor1.on(speed = speed)
            print(self.calibrate_RLI(self.color1), self.calibrate_RLI(self.color4), file = stderr)
            self.motor1.off()
        else: 
            while self.calibrate_RLI(self.color4) < t:
                self.motor2.on(speed = speed)
            self.motor2.off()
        print(self.calibrate_RLI(self.color1), self.calibrate_RLI(self.color4), file = stderr)

    def align_black(self, speed = 20, t = 4.7):
        print("1 ", self.calibrate_RLI(self.color1), self.calibrate_RLI(self.color4), file = stderr)
        while self.calibrate_RLI(self.color1) > t and self.calibrate_RLI(self.color4) > t:
            self.steer_pair.on(steering = 0, speed = speed)
            
        print("2 ", self.calibrate_RLI(self.color1), self.calibrate_RLI(self.color4), file = stderr)
        self.steer_pair.off()
        if self.calibrate_RLI(self.color4) < t:
            while self.calibrate_RLI(self.color1) > t:
                self.motor1.on(speed = speed)
            print("3 ", self.calibrate_RLI(self.color1), self.calibrate_RLI(self.color4), file = stderr)
            self.motor1.off()
        else: 
            while self.calibrate_RLI(self.color4) > t:
                self.motor2.on(speed = speed)
            print("4 ", self.calibrate_RLI(self.color1), self.calibrate_RLI(self.color4), file = stderr)
            self.motor2.off()
        print("5 ", self.calibrate_RLI(self.color1), self.calibrate_RLI(self.color4), file = stderr)

    def align(self, t, speed = -20):
        self.align_white(speed = speed, t = 100 - t)
        self.align_black(speed = -5, t = t)
        self.align_white(speed = -5, t = 100 - t)
    
    def calibrate_RLI(self, color_sensor):
        if (color_sensor.address == INPUT_1):
            black = self._black1
            white = self._white1 
        else:
            black = self._black4
            white = self._white4
        return (color_sensor.reflected_light_intensity - black) / (white - black) * 100

