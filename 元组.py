#python的元组与列表相似，不同之处在于
# 元组的元素不能修改，元组使用小括号，列表使用方括号
pmx=(1,2,3,4,5,6)
print(pmx)
print(pmx[0])
#元组不能修改
#pmx[0]=321

#内置函数count,index
#index,count与字符串和列表的用法相同

#len()
#测量字典中，键值对的个数
##print(len(de))
#keys
#返回一个包含字典所有KEY的“列表”
da=[{"de":12,"as":32},{"sdas":123}]
print(da)
for temp in da:
    a=input("请输入查询键")
    if temp[a]==da:
        print("有此键")

#返回一个包含字典所有的value的列表
#da=[{"de":12,"as":32},{"sdas":123}]
#da.value()
