# 函数的返回值
# 输入名字
#name=input("名字:")
#用户输入名字
#print(name)
#名字：XXX
#当print（name），返回一个输入的名字



def get_wendu():
    wendu=22
    print("当前室温是：%s"%wendu)
    return wendu
def get_wendu_huashi(d):#get_wendu_huashi(b)的参数传递给get_wendu_huashi(a)，所以a才能知道自己变量为22
    huashiwendu=d+30#a的变量为22
    print("当前huashi温度是：%s"%huashiwendu)
c=get_wendu()
get_wendu_huashi(c)

#返回多个值
def bbb():
    a=123
    b=32
    c=56
    #只能返回一个值
    return a
    return b
    return c
ll=bbb()
print(ll)
a=123#只输出第一个值
#解决方法有几种方法
#1.利用列表
def bbb():
    a=123
    b=32
    c=56
    #用一个列表封装3个变量的值
    d=[a,b,c]
    return d
print(bbb())
#第二种,元组的方法封装
    #d=(a,b,c)
    #return d

#第三种
    #d=a,b,c
    #renturn a,b,c

#第四种，列表法
    #renturn [a,b,c]
