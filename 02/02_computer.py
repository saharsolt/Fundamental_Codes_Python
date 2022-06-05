# Gussing number
import random
javab = random.randint(1,99)

hads = int(input('What is your number?'))
name = input('What is your name?')
while hads != javab :
    if hads > javab :
        print ('hads is larger than mine.')
    else : 
        print ('hads is smaller than mine')
    hads = int(input('What is your number?'))

print ('WWWWooooo, you did it!', name , 'You find the number! you rock it!')        