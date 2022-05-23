#If a word has more uppercase letters than lowercase letters, it writes the whole word in uppercase, otherwise it writes the whole word in lowercase letters.
string = input()
count = 0
count1 = 0
for letter in string :
    if letter.islower() == True :
        count = count + 1
    else :
        count1 = count1 + 1
if count1 > count :
    string = string.upper()
else :
    string = string.lower()
print(string)