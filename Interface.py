#-*- coding: UTF-8 -*-

import pygame as pygame
import sys as sys
import Engines as engine
import Keyboard as keyboard
#
#
#还有其他组件需要加在这

def init():
    """初始化"""
    #初始化电机(一个引擎一个舵机)对象，设置状态为停止，并提供报错通道
    try:
        main_engine = engine.Engine(0)
        steer = engine.Engine(0)


    except:
        print('ENGINE INITIALIZATION FAILED')
        input('PRESS ENTER TO QUIT')
        sys.exit()

    #启动pygame界面
    try:
        pygame.init()
        screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption('Console')
    except:
        print('GRAPHIC CONSOLE INITIALIZATION FAILED')
        input('PRESS ENTER TO QUIT')
        sys.exit()
       


def check_event(engine, steer):
    """键盘事件检查"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            keyboard.action_down(event.key, engine, steer)

        elif event.type == pygame.KEYUP:
            keyboard.action_up(event.key, engine, steer)


    
init()
            
#开启循环
while True:
    check_event(main_engine, steer)
    engine.flip(main_engine, steer)
