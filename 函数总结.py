#定义函数，和函数的调用
def a():
    print("*"*50)
    print("  名片管理系统")
    print("1.xxx")
    print("2.xxx")
    print("*" * 50)
#利用函数实现模块化开发
def b():
    print("*"*50)
    print("  名片管理系统")
    print("1.xxx")
    print("2.xxx")
    print("*" * 50)
a()
b()
#函数的参数传递数据
while True:
    def c(a,b):
        #a=10
        #b=20
        result=a+b
        print("%d+%d=%d"%(a,b,result))
    num1=int(input("请输入第一个数"))
    num2 = int(input("请输入第二个数"))
    #调用函数
    c(num1,num2)

#函数的返回值
#输入名字
name=input("名字:")
#用户输入名字
print(name)
#名字：XXX
#当print（name），返回一个输入的名字



def get_wendu():
    wendu=22
    print("当前室温是：%s"%wendu)
    return wendu#return的意思是返回wendu这个值成为函数get_wendu()，等待调用
def get_wendu_huashi(we):
    wendu=we+30
    print("当前huashi温度是：%s"%wendu)
result=get_wendu()
get_wendu_huashi(result)