#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
ev3 = EV3Brick()


ev3.speaker.beep()

motor_izquierdo = Motor(Port.A)
motor_derecho = Motor(Port.D)
robot = DriveBase(motor_izquierdo, motor_derecho, wheel_diameter=55.5, axle_track=104)
sensor_color = ColorSensor(Port.S4)
colores_texto = {
    Color.BLACK: "Negro",
    Color.BLUE: "Azul",
    Color.GREEN: "Verde",
    Color.YELLOW: "Amarillo",
    Color.RED: "Rojo",
    Color.WHITE: "Blanco",
    Color.BROWN: "Marrón",
    None: "naycolor"}

while True:
    color_detectado = sensor_color.color()
    if color_detectado == Color.RED:
        robot.drive (100, 1.2)
        break
    robot.drive (-100, 1.2)


wait(5000)
