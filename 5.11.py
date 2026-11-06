lst=list(map(int,input().split(",")))
n,m=map(int,input().split(","))
if abs(n)>=len(lst):
    print("error")
    quit()
else:
    lst=lst+[lst[n]]*m

print(lst)