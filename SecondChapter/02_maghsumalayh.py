#Function- Divisor
def maghsum(x) :
    count = 0
    for i in range(1,x+1):
    
        if x % i == 0 :
            count = count + 1
    return count
max1 = 0
y = 0
for j in range(20) :
    
    x = int(input())
    maghsum(x)

    if maghsum(x) > max1 :
        max1 = maghsum(x)
        y = x
    if maghsum(x) == max1 :
        if x > y :
            y = x
print( y , max1 )
    