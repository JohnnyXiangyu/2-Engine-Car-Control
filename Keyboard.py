import pygame 

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
