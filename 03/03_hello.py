#Getting an string if you can find Hello in string after deleting some alphabets, print yes

string = input()
string = string.lower()
H = string.find('h')
E = string.find('e',H)
L = string.find('l',E)
A = string.find('l',L+1)
O = string.find('o',A)

if H < E < L < A < O :
    print('YES')
else :
    print('NO')