
# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def test1():
    pass
def test2():
    print('---2-1----')
def test3():
    print('---3-1----')
    test2()
    print('---3-2----')
test3()

def print_line():
    print('-'*5)
def print_5_line():
    i = 0
    while i <= 5:
        print(print_line())
        i += 1
print_5_line()

# 求三个数的平均值

def q(a, b, c):
    result = a + b + c
    return result
def b(a1, b1, c1):
    result1 = q(a1, b1, c1)
    result = result1/3
    print(result)
num1 = int(input('第一个数：'))
num2 = int(input('第二个数：'))
num3 = int(input('第三个数：'))
b(num1, num2, num3)

# 返回多个值 在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
# import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数。然后，我们就可以同时获得返回值：

x,y = move(100,100,60,math)

import math
def quadratic(a, b, c):
    c = [a, b, c]
    for x in c:
        if not isinstance(c, (int, float)):
            raise TypeError('bad operand type')

