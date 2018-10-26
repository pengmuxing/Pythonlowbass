def mingpian():
    print("="*50)
    print("     名片管理系统 V0.01")
    print("1.添加新的名片")
    print("2.删除一个名片")
    print("3.修改一个名片")
    print("4.查询一个名片")
    print("5.显示所有名片")
    print("6.退出系统")
    print("="*50)
mingpian()
#获得用户输入
card_infor=[]
while True:
    #获取用户选择
    num = int(input("请输入操作序号："))
    #根据输入的序号操作相应功能
    if num==1:
        def new_name():
            global card_infor
            new_name=input("请输入新的名字：")
            new_qq=int(input("请输入新的qq："))
            new_weixin=int(input("请输入新的微信："))
            new_addr=input("请输入新的地址：")
            #定义以个新的字典，用来储存信息
            new_infor={}
            new_infor["name"]=new_name
            new_infor["qq"]=new_qq
            new_infor["微信"]=new_weixin
            new_infor["地址"]=new_addr
            #将一个字典，添加到列表中
            card_infor.append(new_infor)
            print(card_infor)
        new_name()
    elif num==2:
        global card_infor
        #获取用户删除的名字
        def del_name():
            del_name=input("请输入删除的名字")
            for temp in card_infor:
                if del_name==temp["name"]:
                    card_infor.remove(temp)
                    print("删除成功")
                    break
                else:
                    print("查无此人")
        del_name()           
    elif num==3:
        #获取用户修改的名字
        xiu_name=input("请输入修改名字")
        for temp in card_infor:
            if xiu_name==temp["name"]:
                temp["name"]=input("请输入新的名字")
                temp["qq"] = input("请输入新的qq")
                temp["微信"] = input("请输入新的微信")
                temp["地址"] = input("请输入新的地址")
                print("修改成功")
                break
    elif num==4:
        #获取用户查询名字，赋值成find_name
        find_name=input("请输入查询名字：")
        #for in 意思是把car_infor里面的元素赋值成temp
        for temp in card_infor:
            #temp[]就是card_infor的键，或者值
            if find_name==temp["name"]:
                print("%s\t%s\t%s\t%s" % (temp["name"], temp["qq"], temp["weixin"], temp["addr"]))
                break
        else:
            print("查无此人")
    elif num==5:
        print("名字\tQQ\t微信\t地址")
        for temp in card_infor:
            print("%s\t%s\t%s\t%s"%(temp["name"],temp["qq"],temp["微信"],temp["地址"]))
            break
    elif num==6:
        print("退出系统")
        break



