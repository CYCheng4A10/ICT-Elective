import math
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
delta = b*b-4*a*c
if delta < 0:
    print('None')
else:
    rootone = (-b+math.sqrt(delta))/(2*a)
    roottwo = (-b-math.sqrt(delta))/(2*a)
    if rootone == roottwo:
        print(f"{roottwo:.3f}")
    elif rootone > roottwo:
        print(f"{roottwo:.3f}", end=" ")
        print(f"{rootone:.3f}")
    else:
        print(f"{rootone:.3f}", end=" ")
        print(f"{roottwo:.3f}")