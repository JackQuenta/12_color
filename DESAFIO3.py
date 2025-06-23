#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()
motor_izquierdo = Motor(Port.A)
motor_derecho = Motor(Port.D)
sensor_color = ColorSensor(Port.S4)

robot = DriveBase(motor_izquierdo, motor_derecho, 55.5, 104)

guardavaloresceroyuno = []

sensor_sobre_linea_negro = False
tiempo = 0
limitetiempoms = 200  

robot.drive(-20, 0)

while len(guardavaloresceroyuno) < 16:  
    color_detectado = sensor_color.color()

    if color_detectado == Color.BLACK:
        if  not sensor_sobre_linea_negro:#por corroborar
            sensor_sobre_linea_negro = True
            tiempo = 0
        else:
            tiempo += 10
    else:
        if sensor_sobre_linea_negro:
            if tiempo >= limitetiempoms:
                guardavaloresceroyuno.append(1)
            else:
                guardavaloresceroyuno.append(0)
            sensor_sobre_linea_negro = False

    ev3.screen.clear()
    ev3.screen.draw_text(10, 50, guardavaloresceroyuno)

    wait(10)

robot.stop()
ev3.speaker.beep()