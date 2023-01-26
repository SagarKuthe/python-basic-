lst=[]
for i in range(5):
    num=int(input("Enter your number :-"))
    if(num>9):
        lst.append(num)
        a=sum(lst)
print(lst)
print(a)
