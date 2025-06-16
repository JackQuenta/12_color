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

# Lista para guardar los datos (0 = línea delgada, 1 = gruesa)
secuencia = []

# Variables de control
sobre_negro = False
contador_negro = 0
grosor = 200  # ms (tiempo mínimo para considerar una línea como gruesa)

# Comenzar a moverse
robot.drive(-20, 0)

while len(secuencia) < 8:  # Leer 8 barras como ejemplo
    color_detectado = sensor_color.color()

    if color_detectado == Color.BLACK:
        if not sobre_negro:
            sobre_negro = True
            contador_negro = 0
        else:
            contador_negro += 10
    else:
        if sobre_negro:
            # Fin de la barra negra, decidir si fue gruesa o delgada
            if contador_negro >= grosor:
                secuencia.append(1)
            else:
                secuencia.append(0)
            sobre_negro = False

    # Mostrar la secuencia actual en pantalla
    ev3.screen.clear()
    ev3.screen.draw_text(10, 50, secuencia)

    wait(10)

robot.stop()
ev3.speaker.beep()