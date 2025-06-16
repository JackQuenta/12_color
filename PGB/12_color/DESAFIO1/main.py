#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()
#Desafío 1: Detector de colores
#Construye un detector de colores. 
#Configura tu ladrillo para que muestre en el display el color de esta detectando el sensor de color.



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
    nombre_color = colores_texto.get(color_detectado, "naycolor")

    ev3.screen.clear()
    ev3.screen.draw_text(10, 50, nombre_color)
wait(5000)
