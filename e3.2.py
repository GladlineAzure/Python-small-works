x=int(input())
if x<50:
    print(f"{x:.1f}")
elif x>=50 and x<100:
    y=x*0.9
    print(f"{y:.1f}")
elif x>=100:
    y=(x-100)*0.8+90
    print(f"{y:.1f}")