x = int(input())
temp = 0
for i in range(1,x+1):
    temp = i**2
    for j in range(x):
        print(str(temp+ i*j), end=" ") 
    print()


