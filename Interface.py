#-*- coding: UTF-8 -*-

import Motor as motor 

#系统检查功能还没做好。。。
print('CONSOLE ONLINE \n')

#定义用户输入字典
cmd_dictionary_1 = {'forward':1, 'backward': -1, 'leftturn': -1, 'stop':0}
cmd_dictionary_2 = {'forward':1, 'backward': -1, 'leftturn': 1, 'stop':0}

#实例化引擎
engine_1 = motor.engine(1, 100, 110, 0, 0)
engine_2 = motor.engine(2, 120, 200, 0, 0)

#主循环
active = True
while active == True:
    print('\n')
    cmd = input('CMD HIER >>> ')
    
    if cmd == 'end session':
        active = False
    else: 
        print('PROCESSING......')

        #获取并处理用户输入
        code = []
        code = cmd.split()

        #报错机制
        if len(code) == 2:
            if code[0] != 'forward' and code[0] != 'backward' and code[0] != 'leftturn' and code[0] != 'rightturn' and code[0] != 'stop' and type(code[1]) is int:
                print('ERROR: WRONG COMMAND')
            else:
                print('PROCESSING COMPLETE')
                #理解两个关键词+更新引擎状态
                engine_1.update_engine(cmd_dictionary_1[code[0]], int(code[1]))
                engine_2.update_engine(cmd_dictionary_2[code[0]], int(code[1]))
        else:
            print('ERROR: WRONG SYNTAX')


print('\nCONSOLE OFFLINE')
