import math
x = int(input())
isSquare = False
if (int(math.sqrt(x)))**2 == x:
    isSquare = True
isTri = False
if (int(math.sqrt(8*x + 1)))**2 == 8*x + 1: #If (8*x + 1) is not a square number, then it is not a triangular number.
    isTri = True

if isTri and isSquare:
    print("Both")
elif isTri:
    print("Triangular")
elif isSquare:
    print("Square")
else:
    print("Neither")
