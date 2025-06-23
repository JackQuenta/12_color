#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
motor_a = Motor(Port.A)
motor_d = Motor(Port.D)
sensor_color = ColorSensor(Port.S4)  

LIMITEBLANCO = 35

VELOCIDAD = 100
while True:
    reflejo = sensor_color.reflection()

    if reflejo > LIMITEBLANCO:
        motor_a.run(VELOCIDAD)
        motor_d.stop()
    else:
        motor_d.run(VELOCIDAD)
        motor_a.stop()

    wait(10)