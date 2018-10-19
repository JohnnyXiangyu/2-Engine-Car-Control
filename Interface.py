#-*- coding: UTF-8 -*-

import pygame as pygame
import sys as sys
import Engines as engine
#
#
#还有其他组件需要加在这

def main():
    """主循环"""
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Console')

    #初始化电机对象
    engine1 = engine.Engine(1)
    engine2 = engine.Engine(2)

    while True:
        check_event(engine1, engine2)
        flip(engine1, engine2)


def check_event(engine1, engine2):
    """键盘事件检查"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            action_down(event.key, engine1, engine2)

        elif event.type == pygame.KEYUP:
            action_up(event.key, engine1, engine2)


def action_down(key, engine1, engine2):
    """响应键盘按下"""
    if key == pygame.K_w:
        engine1.direction = 1
        engine1.speed = 1
        engine2.direction = 1
        engine2.speed = 1

    elif key == pygame.K_a:
        engine1.direction = -1
        engine1.speed = 1
        engine2.direction = 1
        engine2.speed = 1

    elif key == pygame.K_s:
        engine1.direction = -1
        engine1.speed = 1
        engine2.direction = -1
        engine2.speed = 1

    elif key == pygame.K_d:
        engine1.direction = 1
        engine1.speed = 1
        engine2.direction = -1
        engine2.speed = 1


def action_up(key, engine1, engine2):
    """响应键盘抬起"""
    engine1.direction = 1
    engine1.speed = 0
    engine2.direction = 1
    engine2.speed = 0


def flip(engine1, engine2):
    """把程序储存的状态更新到电机上"""
    #需要写上正确的gpio代码
    print('ENGINE', engine1.num, 'IS GOING ON DIRECTION:', engine1.direction, 'AT SPEED OF', engine1.speed)
    print('ENGINE', engine2.num, 'IS GOING ON DIRECTION:', engine2.direction, 'AT SPEED OF', engine2.speed)

main()
