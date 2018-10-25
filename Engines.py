import RPi.GPIO as GPIO
import time
import pygame as pygame

IN1 = 

class Engine():
    """表示电机的类"""
    def __init__(self, status, step, in1, in2, in3, in4):
        """初始化电机的方向和速度变量"""
        self.status = status
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4

    def update(self, direction, speed):
        """在程序中更新电机状态"""
        self.direction = direction
        self.speed = speed


def setup(engine, steering):
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(engine.in1, GPIO.OUT)
	GPIO.setup(engine.in2, GPIO.OUT)
	GPIO.setup(engine.in3, GPIO.OUT)
	GPIO.setup(engine.in4, GPIO.OUT)
    GPIO.setup(steer.in1, GPIO.OUT)
	GPIO.setup(steer.in2, GPIO.OUT)
	GPIO.setup(steer.in3, GPIO.OUT)
	GPIO.setup(steer.in4, GPIO.OUT)


def setStep(w1, w2, w3, w4, engine):
	GPIO.output(engine.in1, w1)
	GPIO.output(engine.in2, w2)
	GPIO.output(engine.in3, w3)
	GPIO.output(engine.in4, w4)


def stop(engine):
	setStep(0, 0, 0, 0, engine)
