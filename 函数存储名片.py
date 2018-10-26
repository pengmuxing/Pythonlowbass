#1.打印功能提
def name():
    print("="*50)
    print("     名片管理系统 V0.01")
    print("1.添加新的名片")
    print("2.删除一个名片")
    print("3.修改一个名片")
    print("4.查询一个名片")
    print("5.显示所有名片")
    print("6.退出系统")
    print("="*50)
#1.打印功能提
names=[] #定义一个空列表来储存添加的名字
while True:
    num=int(input("请输入功能序号："))
    #2.获取用户选择
    if num==1:
        def new_name():
            new_name=input("请输入名字：")
            names.append(new_name)
            print(new_name)
            print(names)
        new_name()
    #删除用户
    elif num==2:
        def del_name():
            name = input("请输入删除名字：")
            names.remove(name)
            print("删除成功")
        del_name()
    #修改用户
    elif num==3:
        def xiu_name():
            # xxx.index()的意思是下标，这里是把用户输入的名字下标，赋值成a
            a=names.index(input("请输入修改的名字"))
            #names[]的意思是names的下标，上个命令是把下标赋值成a，names[a]的意思是找到names的a,最后再赋值成为b.
            b=names[a]
            #这里的意思b是否在names里
            if b in names:
                names[a]=input("请输入新的名字")
                c=names[a]
                print("你的新名字为：%s"%c)
            else:
                print("不存在此人")
        xiu_name()
    elif num==4:
        def cha_name():
            find_name=input("请输入要查询的名字：")
            if find_name in names:
                print("找到了你要找的人")
            else:
                print("查无此人")
        cha_name()
    elif num==5:
        break
    else:
        print("你的输入有误，请重新输入")
name()



