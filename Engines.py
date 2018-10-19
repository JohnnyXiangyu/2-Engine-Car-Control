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
