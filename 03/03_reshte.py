#Saman must write a program that reads a string from the input and applies the following changes to it. Delete all vowels. Print a dot before each silent letter.Write all the remaining silent letters in lower case.

string = input('')
Senc = string.lower()
y = ""

for letter in Senc:
    
    if letter == 'a' :
        Senc = Senc.replace('a','')

    if letter == 'e' :
        Senc = Senc.replace('e','')

    if letter == 'o' :
        Senc = Senc.replace('o','')

    if letter == 'i' :
        Senc = Senc.replace('i','')

    if letter == 'u' :
        Senc = Senc.replace('u','')

for letter in Senc:
    if letter != " " :
        y = y + "." + letter
    else:
       y = y + " " 

print (y)
    