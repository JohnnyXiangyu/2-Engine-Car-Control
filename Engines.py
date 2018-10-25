import RPi.GPIO as GPIO
import time
import pygame as pygame

class Engine():
    """表示电机的类"""
    def __init__(self, status, in1, in2, in3, in4):
        """初始化电机的方向和速度变量"""
        self.status = status
        #Need to add new attribute step for the steer
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4


def setup(engine, steer):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(engine.in1, GPIO.OUT)
    GPIO.setup(engine.in2, GPIO.OUT)
    GPIO.setup(engine.in3, GPIO.OUT)
    GPIO.setup(engine.in4, GPIO.OUT)
    #Add setups of steer!


def step(w1, w2, w3, w4, engine):
    GPIO.output(engine.in1, w1)
    GPIO.output(engine.in2, w2)
    GPIO.output(engine.in3, w3)
    GPIO.output(engine.in4, w4)


def flip(engine, steer):
    if engine.status == 1:
        step(1, 0, 0, 0, engine)
        time.sleep(0.002)
        step(0, 1, 0, 0, engine)
        time.sleep(0.002)
        step(0, 0, 1, 0, engine)
        time.sleep(0.002)
        step(0, 0, 0, 1, engine)
        time.sleep(0.002)
        
    if engine.status == -1:
        step(0, 0, 0, 1, engine)
        time.sleep(0.002)
        step(0, 0, 1, 0, engine)
        time.sleep(0.002)
        step(0, 1, 0, 0, engine)
        time.sleep(0.002)
        step(1, 0, 0, 0, engine)
        time.sleep(0.002)

def stop(engine):
    setStep(0, 0, 0, 0, engine)
