'''
请输入三个数
'''
i = 0
while i < 1:
    a, b, c = map(int, input("请输入三角形三条边:").split(','))
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("等边三角形")
        elif a == c != b or a == b != c or b == c != a:
            print("等腰三角形")
        elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
            print("直角三角形")
        else:
            print("一般三角形")
    else:
        print("无法构成三角形")
        break
