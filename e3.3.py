s=input()
x=int(s)
if (x%4!=0) or (x%100==0 and x%400!=0):
    print(f"In {x} February has 28 days.")
else:
    print(f"In {x} February has 29 days.")