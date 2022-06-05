# getting an input with any combination of Alphabets. If you can find both AB and BA, print yes otherwise print no. ABA: no   
string = input()
key = 'AB'
key1 = 'BA'
counter = 0
counter1 = 0
if string.find(key) == -1 or string.find(key1) == -1 :
    print('NO')
else:
    if string[string.find(key)] == 'A' :
        counter = 1
        string = string[ :string.find(key)] + '  ' + string[string.find(key) + 2 :]
    if string[string.find(key1)] == 'B' :
        counter1 = 1
        string = string[ :string.find(key1)] + '  ' + string[string.find(key1) + 2 :]
    if counter + counter1 == 2 :
        print('YES')
    else :
        print('NO')

