#1
'''20192228
   3月4日作业
   3月4日'''
#2
x=int(input("输入x"))
y=(5*x+8)%(26)
print("y",y)
i=21*(y-8)%26
print("x",i)
#3
a=int (input("输入a"))
n=int (input("输入n"))
q=int (input("输入q"))

s=a*q

b=a*((q**n)-1)/(q-1)
if n<1:
    print("sn   ",s)
if n>=1:
    print("sn   ", b)