import random
import string

# 挑战1：批量生成密码文件
def bulk_generate():
    weak_passwords = ["admin",'123456','qwerty','password']
    with open("passwords.txt","w") as f:
        for _ in range(10):
            pwd = random.choice(weak_passwords)+str(random.randint(100,999))
            f.write(pwd+"\n")
    print("挑战1完成：已生成passwords.txt")

# 挑战2：自定义密码+后缀
def custom_password():
    base = input("请输入基础密码（如姓名/生日）：")
    suffixes = [str(random.randint(1000,9999)) for _ in range(5)]
    print("挑战2的结果：", [base + s for s in suffixes])

# 挑战3：复杂度检查
'''
    ''.join(...) 将字符列表拼接为字符串
    random.choices(字符集, k=长度) 从指定字符集中随机选取指定长度的字符
    any(c.isupper() for c in password) 检查密码中是否存在至少一个大写字母
'''
def complex_password():
    while True:
        pwd = ''.join(random.choices(string.ascii_letters + string.digits,k=8))
        if any(c.isupper() for c in pwd):
            print("挑战3合格密码：",pwd)
            break
print(complex_password())