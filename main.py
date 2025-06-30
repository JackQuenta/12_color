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
ev3.speaker.beep()

motor_derecho = Motor(Port.A)
motor_izquierdo = Motor(Port.D)
sensor_color = ColorSensor(Port.S4)

velocidad_base = 170  

while (True): #LOOP FOREVER
    reflejo = sensor_color.reflection()
    estado = reflejo
    

    if estado >=0 and estado<=20:
        potencia_izq = 80
        potencia_der = 10
    elif estado >20 and estado<=40:
        potencia_izq = 80
        potencia_der = 60
    elif estado >40 and estado<=60:
        potencia_izq = 80
        potencia_der = 80
    elif estado >60 and estado<=80:
        potencia_izq = 60
        potencia_der = 80
    elif estado >80 and estado<=100:
        potencia_izq = 10
        potencia_der = 80

    velocidad_izq =  (potencia_izq * velocidad_base) // 100
    velocidad_der =  (potencia_der * velocidad_base) // 100

    motor_izquierdo.run(velocidad_izq)
    motor_derecho.run(velocidad_der)

    wait(10)
