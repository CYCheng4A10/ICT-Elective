import math
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
delta = math.sqrt(b*b-4*a*c)
rootone = float((-b+delta)/(2*a))
roottwo = float((-b-delta)/(2*a))
if delta < 0:
    print('None')
elif rootone == roottwo:
    print(str(rootone))
else:
    print(round(str(rootone), 3), end=" ")
    print(round(str(roottwo), 3))
