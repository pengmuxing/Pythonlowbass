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