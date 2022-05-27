# Getting a number as an input and printing 2 * its digits in reverse order.
X = int(input())
Y = X % 10
Z = (X // 10) % 10
W = X // 100  
print (2 * int (str (Y) + str (Z) + str (W)))