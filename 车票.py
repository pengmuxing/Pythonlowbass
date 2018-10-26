#encoding=utf-8
chepiao=1
knife=9
if chepiao==1:
    print("有车票，过安检！！")
    if knife>=10:
        print("刀子长度太长，不给上车")
    else:
        print("上车，出发！！")
else:
    print("没车票，不准上车")
    print("没车票，不准上车")


#encoding=utf-8
yu_e=2
zuowei=1
if yu_e>=2:
    print("可以上车")
    if zuowei>0:
        print("可以坐下")
elif yu_e<2:
    print("余额不足，请及时充值")
