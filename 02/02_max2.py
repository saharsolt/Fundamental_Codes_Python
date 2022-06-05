# Finding first  and second maximum number
x = int (input())
y = int (input())

if x > y :
    max1 = x
    max2 = y
elif x < y :
    max1 = y
    max2 = x

while x != -1 :
    
    x = int(input())
    if x > max1 :
        max2 = max1
        max1 = x
    else :
        if  x > max2 :
            max2 = x
        
print (max1, max2) 