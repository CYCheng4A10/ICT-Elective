n = input()
firstDigit = n[0] #check the first character of the string
if firstDigit in ('2', '3'):
    print('Fixed')
elif firstDigit in ('5','6','9'):
    print('Mobile')
