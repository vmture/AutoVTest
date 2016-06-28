#-*- coding: utf-8 -*-
__author__ = 'vmture'
# import sys,cmd
# class PY(cmd.Cmd):
#     def __init__(self):            #初始基础类方法
#         cmd.Cmd.__init__(self)
#
#     def help_hello(self):
#         print("输入hello 参数，将执行o_hello方法，输出参数值")
#
#     def do_hello(self,line):
#         print("do_hello:",line)
#
#     def help_exit(self):          #以help_*开头的为帮助
#         print("输入exit退出程序")
#
#     def do_exit(self,line):       #以do_*开头为命令
#         print("Exit:",line)
#         sys.exit()
#
# if __name__ =="__main__":
#     cmd = PY()
#     cmd.cmdloop()

# import os
# class StartAppium():
#     def cmd_start(self):
#         os.system('cmd /k start /b appium')
#
#     def cmd_stop(self):
#         os.system('taskkill /f /im node.exe')
#
#     def shell_start(self):
#         pass
#
#     def shell_stop(self):
#         pass

import subprocess
import time
class StartAppium():
    def cmd_start(self):
        subprocess.Popen('cmd /k start /b appium')
        time.sleep(5)

    def cmd_stop(self):
        subprocess.Popen('taskkill /f /im node.exe')
        time.sleep(5)

    def shell_start(self):
        pass

    def shell_stop(self):
        pass

# if __name__ == '__main__':
#     a=StartAppium()
#     a.cmd_start()
#     time.sleep(1)
#     print('1')
#     time.sleep(1)
#     print('2')
#     time.sleep(1)
#     print('3')
#     time.sleep(1)
#     print('4')
#     a.cmd_stop()
#     print('quit')