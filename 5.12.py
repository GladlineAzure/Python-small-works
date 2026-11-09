a=input()
n=int(a)
p=0
found=False
for q in range(100,n+1):
    lst=[int(i) for i in str(q)]
    p=0
    for j in lst:
        p=j**3+p
    if p==q:
            found=True
            print(q)


if not found:
        print("none")
