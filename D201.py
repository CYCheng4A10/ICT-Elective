x = int(input())
b = 1
new = 0
if x > 0:
  for i in range(x):
    new = b + new
    b = new - b
  print(new)
else:
  print('0')
