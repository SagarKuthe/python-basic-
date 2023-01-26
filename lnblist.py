L1=[11,21,24,12,18]
L2=[14,44,25,37,13]
L3=[]
i=0
while(i<len(L1)):
    a=L1[i]
    L3.append(a)
    i=i+2
i=1
while(i<len(L2)):
    b=L2[i]
    L3.append(b)
    i=i+2

print(L3)
