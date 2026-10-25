x=int(input())
y=0
m=0
n=0
if x%5==0 and x%7==0 and x%11==0:
    print(f"{x} can divided by 5,7 and 11.")
elif x%5==0 or x%7==0 or x%11==0:
    if x%5==0:
        y=5
    if x%7==0:
        m=7
    if x%11==0:
        n=11
    if y!=0:
        print(f"{x} can divided by {y}.")
    if m!=0:
        print(f"{x} can divided by {m}.")
    if n!=0:
        print(f"{x} can divided by {n}.")
else:
    print(f"{x} can not divided by 5,7 or 11.")