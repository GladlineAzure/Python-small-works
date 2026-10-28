a=int(input())
b=int(input())
x=(a-b)/b
if a<=b:
    print("未超速")
elif 0<x<=0.1:
    print("超速警告")
elif 0.1<x<=0.2:
    print("罚款100元")
elif 0.2<x<=0.5:
    print("罚款500元")
elif 0.5<x<=1:
    print("罚款1000元")
elif x>1:
    print("罚款2000元")
