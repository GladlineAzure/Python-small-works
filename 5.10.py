lst1=eval(input())
lst2=[]
for i in lst1:
    if i<=1:
        continue
    flag=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            flag=False
            break
    if flag:
        lst2.append(i)
print(lst2)
            