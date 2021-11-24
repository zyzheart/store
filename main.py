'''
任务：如果键盘输入大于随机数弹出友好提示信息“猜大了”，猜小了
起始金额  5000 才对一次给300 猜错扣除100 猜错15次结束
'''

import random

# 生成随机数
summoney:int = 5000

i = 0
while True:

    Ran = random.randint(1, 20)
    print(Ran)
    num = input("请输入一个数")

    num = int(num)
    print(Ran)
    if num == Ran:
        print("you are good")
        summoney += 300
    elif num > Ran:
        print("猜数大了")
        i += 1
        summoney -= 100
    elif num is None:
        print("6666666sb")
    else:
        print("猜数小了")
        i += 1
        summoney -= 100
    if i == 15:
        print("狗熊，你输了15次了")
        break
    print("总共钱数")
    print(summoney)
