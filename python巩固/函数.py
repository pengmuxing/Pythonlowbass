# 定义函数和函数的调用
def print_menu():
    print('='*50)
    print('名片管理系统')
    print('1:XXX')
    print('2.XXX')
    print('='*50)
def print_sanjiaoxing():
    print('*')
    print('*'*2)
    print('*'*3)
    print('*'*4)

print_menu()
print_sanjiaoxing()
# 无法重复使用的函数
def sum_p():
    a = 1
    b = 2
    c = a + b
    print('%d+%d=%d' % (a, b, c))
sum_p()

# 函数的参数传递数据,参数的个数，顺序（类型）要相同
def sum_p2():
    a = 1
    b = 3
    result = a + b
    print('%d+%d=%d' % (a, b, result))
s = int(input('请输入第一个数：'))
d = int(input('请输入第二个数：'))
print(sum_p2(s,d))

# 函数的返回值
def get_wendu():
    wendu = 21
    print('当前温度是：%d' % wendu)
def get_huashiwendu(wendu):
    wendu = wendu + 3
    print('当前华氏温度是：%s' % wendu)
wendu = get_wendu()
get_huashiwendu(wendu)

def get_wendu():
    wendu1 = 1

def get_huashiwendu(wendu1):
    huashiwendu = wendu1 + 22

wendu = get_wendu()
get_huashiwendu(wendu)