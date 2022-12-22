list = input().split()
w = float(list[0])
h = float(list[1])
bmi = f'{w/h**2:.3f}'
print(bmi)