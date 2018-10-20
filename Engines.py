class Engine():
    """表示电机的类"""
    def __init__(self, num):
        """初始化电机的方向和速度变量"""
        self.direction = 1
        self.speed = 0
        self.num = num

    def update(self, direction, speed):
        """在程序中更新电机状态"""
        self.direction = direction
        self.speed = speed


def flip(engine1, engine2):
    """把程序储存的状态更新到电机上"""
    #需要写上正确的gpio代码
    print('ENGINE', engine1.num, 'IS GOING ON DIRECTION:', engine1.direction, 'AT SPEED OF', engine1.speed)
    print('ENGINE', engine2.num, 'IS GOING ON DIRECTION:', engine2.direction, 'AT SPEED OF', engine2.speed)
