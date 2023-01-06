n = int(input())
for j in range(0,100,10):
    list = []
    for i in range(1, 11):
        if (j+i)%n == 0 or (j+i)//10 == n or (j+i)%10 == n:
            list.append('Clap')
        else:
            list.append(str(j+i))
    print(' '.join(list))
