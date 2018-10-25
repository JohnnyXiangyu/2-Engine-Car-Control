import pygame 
import Engines as engines

def action_down(key, engine, steer):
    """响应键盘按下"""
    if key == pygame.K_w:
        engine.status = 1

    elif key == pygame.K_s:
        engine.status = -1


def action_up(key, engine, steer):
    """响应键盘抬起"""
    if key == pygame.K_w or key == pygame.K_s:
        engine.status = 0
