class engine():
    """代表引擎属性的类"""
    def __init__(self, num, pin_1, pin_2, status, speed):
        """初始化状态和速率属性"""
        self.status = 0
        self.speed = 0
        self.num = num
        self.pin_1 = pin_1
        self.pin_2 = pin_2
        #在这里需要额外加入的代码：电机端口输出至静止位置

        #表示电机上线
        print('ENGINE_', self.num, ' ONLINE, @ PIN:', self.pin_1, ' & PIN:', self.pin_2)

    def update_engine(self, status, speed):
        """更新属性"""
        self.status = status
        self.speed = speed 
        self.apply_change()

    def apply_change(self):
        #添加代码用来输出端口
        print(self.num, self.status, self.speed)
