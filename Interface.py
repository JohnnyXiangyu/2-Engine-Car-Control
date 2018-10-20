#-*- coding: UTF-8 -*-

import pygame as pygame
import sys as sys
import Engines as engine
import Keyboard as keyboard
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
        engine.flip(engine1, engine2)


def check_event(engine1, engine2):
    """键盘事件检查"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            keyboard.action_down(event.key, engine1, engine2)

        elif event.type == pygame.KEYUP:
            keyboard.action_up(event.key, engine1, engine2)


main()
