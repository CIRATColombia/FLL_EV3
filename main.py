#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Color, Port
from pybricks.ev3devices import Motor
from line_Follower import line
from giro import giro
# Create your objects here

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Play beep sound.
ev3.speaker.beep(frequency=1000, duration=500)

ev3.light.on(Color.RED)

giro(45)

giro(-45)
