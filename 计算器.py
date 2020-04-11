'''2019228
   计算器实验'''
print("功能：1加法 2减法 3乘法 4除法 5乘方（开根号）6取对数")
a=int(input("选择您需要的算法"))
b=float(input(":请输入第一个数"))
c=float(input(":请输入第二个数"))
if a==1 :
    d=b+c
    print(b,"+",c,"=",d)
elif a==2 :
    d=b-c
    print(b,"-",c,"=",d)
elif a==3 :
    d=b*c
    print(b,"X",c,"=",d)
elif a==4 :
    d=b/c
    print(b,"÷",c,"=",d)
elif a==5 :
    d = b**c
    print(b, "^", c, "=", d)
elif a==6 :
    import math
    x=math.log(c)
    y=math.log(b)
    d=x/y
    print("log",b,c,"=",d)

