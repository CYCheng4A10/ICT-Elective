x = int(input())
temp = 1
for i in range(x):
    print(temp, end=" ")
    for j in range(x-1):
      temp = temp + 4
      print(str(temp), end=" ")
    print()