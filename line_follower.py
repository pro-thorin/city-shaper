#!/usr/bin/env python3
# This script will follow the RIGHT EDGE of a black line.
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import ColorSensor
from time import sleep

# Connect an EV3 color sensor to any sensor port.
cl = ColorSensor()
tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)

wf = .5# Use wheel factor = 1 for home version and 0.77 for edu version.
while True:    # forever
    if cl.reflected_light_intensity<30:   # weak reflection so over black line
        # medium turn right
        tank_pair.on(left_speed=50*wf, right_speed=15)
    else:   # strong reflection (>=30) so over white surface
        # medium turn left
        tank_pair.on(left_speed=15, right_speed=50*wf)
    sleep(0.02) # wait for 0.02 seconds
