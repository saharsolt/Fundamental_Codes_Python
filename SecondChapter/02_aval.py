#getting an int as input and printing it is prime or not
x = int (input())
count = 0

for i in range(1,x+1) :
    if x % i == 0 :
        count = count + 1

if count == 2 :
    print ('prime')
else :
    print ('not prime')
