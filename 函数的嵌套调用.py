def a():
    print("*"*50)
def b():
    print("*"*50)
    a()#  嵌套a()
b()

# 利用函数的调用，实现三个值的求和
def d(a,b,c):  # 形参
    d = a+b+c
    print("%d+%d+%d=%d" % (a, b, c, d))
    return d
def c(a2, a3, a4 ):  # 实参
    e = d(a2, a3, a4)  # 形参
    e = e/3
    print("平均值为：%d"%e)
nums1 = int(input("请输入第一个数："))
nums2 = int(input("请输入第二个数："))
nums3 = int(input("请输入第三个数："))
c(nums1, nums2, nums3)#  实参
