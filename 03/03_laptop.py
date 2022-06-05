#2
#1 10
#7 3
# compare 2 laptops or n laptops, print happy risa if you can find two laptop that a laptop with less price has a better quality.
new = []
n = int(input())
l = []
s = []
ss = []
count = 0
count1 = 0
count2 = 0
gheymat = []
keyfiat = []
for i in range(n):
    l.append(input())
for i in range(n):
    s = l[i].split()
    s = list(map(int,s))
    ss.extend(s)
for i in range(2*n) :
    if i % 2 != 0 :
        keyfiat.append(ss.pop())
    else :
        gheymat.append(ss.pop())
for i in range(n) :
    if gheymat[i] < keyfiat[i] :
        count = 1
    elif gheymat[i] > keyfiat[i] :
        count1 = 1
    elif gheymat[i] == keyfiat[i] :
        count2 = 1
if count + count1 + count2 >= 2 :
    print('happy irsa')
else :
    print('poor irsa')


