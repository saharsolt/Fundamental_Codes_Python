# is it plaindrome or not?
string = input()
string = string.lower()
L = len(string)
j = L-1

for i in range(int(L/2)) :
    if string[i] == string[j] :
        i = i + 1
        j = j - 1
        if j <= i :
            print('palindrome')
    else :
        print('not palindrome')
        break