#encoding=utf-8
i=1
while i<=5:
    j=1
    while j<=i:
        print ("*",end="")
        j+=1
    print("")
    i+=1


num=1
while num<=5:
    d=1
    while d<=2:
        print("*",end="")
        d+=1
    print("")
    num+=1

b=1
while b<=9:
    c=1
    while c<= 9:
        d=b*c
        print("%d*%d=%d "%(b,c,d),end="")
        c+=1
        print("")
    b+=1
