import random

key = int(input('What is your number?'))
x = 1
y = 99
hads = random.randint(x,y)
print ('hads of computer is', hads)

if hads > key :
    javab = input ('b ro vared kon ')

elif hads < key : 
    javab = input ('k ro vared kon ')

else :
    javab = input ('d ro vared kon ')

while javab != 'd' :

    if javab == 'b' :
        y = hads - 1
        hads = random.randint(x,y)
        print ('hads of computer is ', hads)

    elif javab == 'k' :
        x = hads + 1
        hads = random.randint(x,y)
        print ('hads of computer is ', hads)

    if hads > key :
        javab = input ('b ro vared kon ')
    
    elif hads < key : 
        javab = input ('k ro vared kon ')
    
    else :
        javab = input ('d ro vared kon ')

print('you did it!', hads , 'equals my number!')
print ('WWWWooooo, you did it! You find the number! you rock it!')        