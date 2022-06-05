#With x1 x2 x3 in hand, calculate the minimum distance these three must travel in total to meet at one point. If the answer to the number is correct, please print it without the decimal point, for example, if you print 6.0 in the following example, it is incorrect.
l = input()
space_split = l.split()
space_split = list(map(float,space_split))
space_split.sort()
S = (space_split[1] - space_split[0]) + (space_split[2] - space_split[1])
S = int(S)
print(S)

