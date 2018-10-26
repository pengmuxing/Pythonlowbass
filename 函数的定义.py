# 定义函数，和函数的调用
def a():
    print("*"*50)
    print("  名片管理系统")
    print("1.xxx")
    print("2.xxx")
    print("*" * 50)
# 利用函数实现模块化开发
def b():
    print("*"*50)
    print("  名片管理系统")
    print("1.xxx")
    print("2.xxx")
    print("*" * 50)
a()
b()

# 四种函数的类型
# 无参数，有返回值
# 有参数，无返回值
# 有参数，有返回值

# def abc()
    #pass
# def()
    #return xxx
# def(参数)
    #pass
# def(参数)
    #return xxx

# 定义一个函数
def abc(a,b):
    #a=1
    #b=2
    c=a+b
    print("%d+%d=%d"%(a,b,c))
nums1 = int(input("请输入第一个数："))
nums2 = int(input("请输入第二个数："))
abc(nums1, nums2)