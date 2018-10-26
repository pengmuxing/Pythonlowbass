#encoding=utf-8
mingpian=[]
while True:
    num1=int(input("请输入功能号："))
    if num1==1:
        newsname=input("请输入新的名字")
        newsqq=int(input("请输入新的QQ"))
        newsadd=input("请输入新的地址")
        cardinfor={}
        cardinfor["name"]=newsname
        cardinfor["qq"]=newsqq
        cardinfor['add']= newsadd
        mingpian.append(cardinfor)
        print(mingpian)

    elif num1==2:
        delname=input("请输入要删除的名字")
        for temp in mingpian:
            if temp["name"]==delname:
                mingpian.remove()
                print("删除成功")
            else:
                print("查无此人")
    elif num1==3:
        xiuname=input("请输入修改的名字")
        for temp in mingpian:
            if temp["name"] ==xiuname:
                temp["name"]==input("请输入新的名字")
                temp["qq"] ==input('请输入新的QQ')
                temp["add"]==input("请输入新的地址")
                print("%s %d %s"%temp["name"],temp["qq"],temp["add"])
            else:
                print("没有找到你要修改的名字")
    elif num1==4:
        findname=input("请输入你要查询的名字")
        for temp in mingpian:
            if temp["name"]==findname:
                print("%s\t%d\t%s" % temp["name"], temp["qq"], temp["add"])
            else:
                print("查无此人")