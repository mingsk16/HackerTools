#弱密码生成器
import random  #导入随机数模块
weak_passwords = ["admin","password","123456","qwerty"] #预定弱密码列表

def generate_password():
    #从弱密码列表中随机选一个 + 3位随机数字
    return random.choice(weak_passwords)+str(random.randint(100,999))
#random.choice("sdfasdf")从序列中随机挑选一个函数 str()转成字符串 random.randint生成一个随机整数
print("黑客专用弱密码生成器v0.1") # 打印工具名称
print("生成的密码：", generate_password()) # 调用函数生成密码并输出