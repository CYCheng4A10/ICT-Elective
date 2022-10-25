import math
price=input()[1:]
price=float(price)
bus_fair= str(math.ceil(price/2*10)/10)
print("$"+bus_fair)
