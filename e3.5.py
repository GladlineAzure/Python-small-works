x=float(input())
y=0
if x>=10000:
    y=x*0.05
elif x>=5000:
    y=x*0.03
elif x>=1000:
    y=x*0.02
elif x<1000:
    y=0
print(f"{y:.2f}")  