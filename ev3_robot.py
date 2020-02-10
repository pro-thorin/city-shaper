#!/usr/bin/env micropython
from ev3dev2.motor import OUTPUT_C, OUTPUT_B, OUTPUT_A, MoveSteering, LargeMotor, MoveTank
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor, ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_4
from time import sleep
from ev3dev2.led import Leds
from ev3dev2.button import Button

# creates a class of Blackberry and Raspberry

class Ev3Robot:

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
        self.gyro.mode = 'GYRO-ANG'
        self.led = Leds()
        self.btn = Button()

    def write_color(self, file, value):
        # opens a file 
        f = open(file, "w")
        # writes a value to the file
        f.write(str(value))
        f.close()

    def read_color(self, file):
        # opens a file
        f = open(file, "r")
        # reads the value
        color = int(f.readline().strip())
        f.close()
        return color

    def pivot_right(self, degrees, speed = 20):
        # makes the robot pivot to the right until the gyro sensor 
        # senses that it has turned the required number of degrees
        self.tank_pair.on(left_speed = speed, right_speed = 0)
        self.gyro.wait_until_angle_changed_by(degrees - 10)
        self.tank_pair.off()
    
    def pivot_left(self, degrees, speed = 20):
        # makes the robot pivot to the left until the gyro sensor 
        # senses that it has turned the required number of degrees
        self.tank_pair.on(left_speed = 0, right_speed = speed)
        self.gyro.wait_until_angle_changed_by(degrees - 10)
        self.tank_pair.off()
    
    def old_spin_right(self, degrees, speed = 20):
        #old program; don't use
        self.gyro.reset()
        value1 = self.gyro.angle
        self.tank_pair.on(left_speed = speed, right_speed = speed * -1)
        self.gyro.wait_until_angle_changed_by(degrees)
        value2 = self.gyro.angle
        self.tank_pair.on(left_speed = -30, right_speed = 30)
        self.gyro.wait_until_angle_changed_by(value1 - value2 - degrees)
        self.stop()
    
    def old_spin_left(self, degrees, speed = 20):
        #old program; don't use
        value1 = self.gyro.angle
        self.tank_pair.on(left_speed = speed * -1, right_speed = speed)
        self.gyro.wait_until_angle_changed_by(degrees)
        value2 = self.gyro.angle
        self.tank_pair.on(left_speed = 8, right_speed = -8)
        self.gyro.wait_until_angle_changed_by(value2 - value1 - degrees + 5)
        self.tank_pair.off()

    def go_straight_forward(self, cm, speed = 20):
        value1 = self.motor1.position
        angle0 = self.gyro.angle
        rotations = cm / 19.05 #divides by circumference of the wheel

        # calculates the amount of degrees the robot has turned, then turns the 
        # opposite direction and repeats until the robot has gone the required 
        # number of centimeters
        while abs(self.motor1.position - value1) / 360 < rotations:
            angle = self.gyro.angle - angle0
            self.steer_pair.on(steering = angle * -1, speed = speed *-1)
        self.steer_pair.off()

    def go_straight_backward(self, cm, speed = 20):
        # see go_straight_forward
        value1 = self.motor1.position
        angle0 = self.gyro.angle
        rotations = cm / 19.05
        while abs(self.motor1.position - value1) / 360 < rotations:
            angle = self.gyro.angle - angle0
            self.steer_pair.on(steering = angle * 1.3, speed = speed)
        self.steer_pair.off()

    def calibrate(self):
        # turns the led lights orange, and waits for a button to be pressed 
        # (signal that the robot is on black), then calculates the reflected 
        # light intensity of the black line, then does the same on the white line 
        self.led.set_color('LEFT', 'ORANGE')
        self.led.set_color('RIGHT', 'ORANGE')
        while not self.btn.any():
            sleep(0.01)
        self.led.set_color('LEFT', 'GREEN')
        self.led.set_color('RIGHT', 'GREEN')
        self._black1 = self.color1.reflected_light_intensity
        self._black4 = self.color4.reflected_light_intensity
        sleep(2) 
        self.led.set_color('LEFT', 'ORANGE')
        self.led.set_color('RIGHT', 'ORANGE')

        while not self.btn.any():
            sleep(0.01)
        self.led.set_color('LEFT', 'GREEN')
        self.led.set_color('RIGHT', 'GREEN')
        self._white1 = self.color1.reflected_light_intensity
        self._white4 = self.color4.reflected_light_intensity
        sleep(3)
        self.write_color("/tmp/black1", self._black1)
        self.write_color("/tmp/black4", self._black4)
        self.write_color("/tmp/white1", self._white1)
        self.write_color("/tmp/white4", self._white4)
    
    def read_calibration(self):
        # reads the color files
        self._black1 = self.read_color("/tmp/black1")
        self._black4 = self.read_color("/tmp/black4")
        self._white1 = self.read_color("/tmp/white1")
        self._white4 = self.read_color("/tmp/white4")

    def align_white(self, speed = 20, t = 96.8):
        # goes forward until one of the color sensors sees the white line. 
        while self.calibrate_RLI(self.color1) < t and self.calibrate_RLI(self.color4) < t:
            self.steer_pair.on(steering = 0, speed = speed)
        self.steer_pair.off()
        # determines which sensor sensed the white line, then moves the opposite 
        # motor until both sensors have sensed the white line
        if self.calibrate_RLI(self.color4) > t:
            while self.calibrate_RLI(self.color1) < t:
                self.motor1.on(speed = speed)
            self.motor1.off()
        else: 
            while self.calibrate_RLI(self.color4) < t:
                self.motor2.on(speed = speed)
            self.motor2.off()

    def align_black(self, speed = 20, t = 4.7):
        # see align_white
        while self.calibrate_RLI(self.color1) > t and self.calibrate_RLI(self.color4) > t:
            self.steer_pair.on(steering = 0, speed = speed)
        self.steer_pair.off()
        if self.calibrate_RLI(self.color4) < t:
            while self.calibrate_RLI(self.color1) > t:
                self.motor1.on(speed = speed)
            self.motor1.off()
        else: 
            while self.calibrate_RLI(self.color4) > t:
                self.motor2.on(speed = speed)
            self.motor2.off()

    def align(self, t, speed = -20):
        # aligns three times for extra accuracy
        self.align_white(speed = speed, t = 100 - t)
        self.align_black(speed = -5, t = t)
        self.align_white(speed = -5, t = 100 - t)
    
    def calibrate_RLI(self, color_sensor):
        # returns a scaled value based on what black and white are
        if (color_sensor.address == INPUT_1):
            black = self._black1
            white = self._white1 
        else:
            black = self._black4
            white = self._white4
        return (color_sensor.reflected_light_intensity - black) / (white - black) * 100

    def stop(self):
        self.tank_pair.off()
    
    def spin_right(self, degrees, speed = 30):
        self.turn(degrees, 100, speed)

    def spin_left(self, degrees, speed = 30):
        self.turn(degrees, -100, speed)

    def turn(self, degrees, steering, speed=30):
        # turns at a decreasing speed until it turns the required amount of degrees
        value1 = self.gyro.angle
        s1 = speed
        d1 = 0
        while d1 < degrees - 2:
            value2 = self.gyro.angle
            d1 = abs(value1 - value2)
            slope = speed / degrees
            s1 = (speed - slope * d1) * (degrees / 90) + 3 
            self.steer_pair.on(steering = steering, speed = s1)
        self.steer_pair.off()
