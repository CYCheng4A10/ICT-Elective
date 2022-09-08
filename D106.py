n = int(input())
if n%100 in (11,12,13):
  suffix = 'th'
elif n%10 == 1:
    suffix = 'st'
elif n%10 == 2:
      suffix = 'nd'
elif n%10 == 3:
    suffix = 'rd'
else:
    suffix = 'th'
print(f'{n}{suffix}')

    
    