""" The first input line shows the number n, getting n numbers and calculating the square root of each input.
Input
4
1
2
19
100

Output
1.0000
1.4142
4.3588
10.0000
"""
from math import sqrt
from decimal import *
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

for letter in l:
    l1 = sqrt(letter)
    print (Decimal(l1).quantize(Decimal(".0001"), rounding=ROUND_DOWN))