#def a():
    #a=100（这里的变量是局部变量）
    #print("a")
#def b():
    #print("%d"%a)由于这里的a变量没有被定义，运行会出现错误
#b()

#使用全局变量解决问题
a=100
def b():
    print("%d"%a)
b()


wendu=100
def a():
    #如果wendu这个变量已经在全局变量里定义了，此时还想在函数中对全局变量进行修改，可以使用global，就可以对全局变量进行修改
    global wendu
    wendu=110
