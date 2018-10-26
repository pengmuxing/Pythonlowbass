#ending=utf-8
names=["孙悟空","唐僧","沙师弟","猪八戒"]
# 字符串中下标的访问，0是开始的第一个元素
print(names[0])
#访问下标从0开始到末尾
print(names[0:])
#下表访问从第一个数到第5个数的前一位
print(names[0:4])
#起步位置，终止位置，步长
print(names[0:4:2])
#计算names的长度
print(len(names))
#负数下标，-1代表最后一位数的前一位,只是在切片的情况下-1代表最后一位的前一位
print(names[0:-1])
#代表列表的最后一位元素，与切片的-1是不一样的
print(names[-1])

#列表的插入与添加
#在names列表中添加元素
names.append("白龙马")
#在names列表中插入一个元素，names.insert(位置，添加的内容)
names.insert(0,"白骨精")

#列表相加
names1=["12","333","456"]
names2=names+names1
print(names2)
#或者用extend
names2.extend(names1)
print(names2)
#删除,只能使用下标删除
names2.pop(-1)
print(names2)
#del删除列表元素
del names2[0]
print(names2)
#in，not in 用于查找列表中是否存在某个元素
if "唐僧" in names2:
    print("找到了")
if "大宝剑" not in names2:
    print("可以添加")

#列表
#1.添加新的元素
#2.append()
#3.insert()
#4.extend()
#删除元素
#pop()-----------删除最后一个
#remove()---------------根据内容删除
#del xxx[下标]=new值
#查询
#in
#not in