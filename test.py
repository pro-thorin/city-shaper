#!/usr/bin/env micropython
from ev3dev2.motor import OUTPUT_C, OUTPUT_B, OUTPUT_A, OUTPUT_D, MoveSteering, LargeMotor, MoveTank, MediumMotor
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor, ColorSensor
from sys import stderr
from ev3_robot import Ev3Robot
#!/usr/bin/env micropython
from ev3dev2.motor import OUTPUT_C, OUTPUT_B, OUTPUT_A, OUTPUT_D, MoveSteering, LargeMotor, MoveTank, MediumMotor
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor
from sys import stderr
from ev3_robot import Ev3Robot

robot = Ev3Robot()
tank_pair = MoveTank(OUTPUT_C, OUTPUT_B)
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
medium_motorA = MediumMotor(OUTPUT_A)
medium_motorD = MediumMotor(OUTPUT_D)

# Mission 4
medium_motorD.on_for_degrees(degrees = 135, speed = 30)
robot.go_straight_forward(45, speed = -20)
robot.spin_right(45)
robot.go_straight_forward(40, -20)
robot.spin_right()

# # Mission 8
# robot.spin_right(degrees = 50)
# robot.go_straight_forward(cm = 91.44)
# robot.spin_right(degrees = 30)
# robot.go_straight_forward(12.5)
# robot.align(t = 92)
# robot.go_straight_forward(38.17)
