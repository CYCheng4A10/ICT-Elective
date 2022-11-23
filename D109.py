x = int(input())
M = [1000, 500, 100, 50, 20, 10]
A = [None]*6
y = 0
for i in M:
    A[y] = x//i
    x = x - i*A[y]
    y += 1
for j in range(len(A)):
    while A[j] > 0:
        print(M[j])
        A[j] -= 1