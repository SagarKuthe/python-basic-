lst=[]
i=0
while(i<4):
    inp=input("Enter your value")
    lst.append(inp)
    tpl=tuple(lst)
    i=i+1
print(tpl)
inp1=input('enter your value')
a=list(tpl)
i=0
while(i<len(a)):
    a.insert(i+1,inp1)
    i=i+2
b=tuple(a)
print(b)
