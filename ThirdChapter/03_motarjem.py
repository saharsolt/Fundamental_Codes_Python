# In the first line of input there is an n number that indicates the number of words in the dictionary. Each of the next n lines contains two words, indicating that the second word means the first word. The next line contains a sentence. A sentence consists of several words separated by space. Now you have to help the translator and write a translator who reads the dictionary and the relevant sentence from the input and translates the sentence. In the translation process, if there is no word in the dictionary, print the word in the output.

import collections

n = int(input())
word = []
this_one = collections.OrderedDict()
s = []
key = []
tarjome = []
sentence = ''
for i in range(n):
     word.append(input())
string = input()
s = string.split()

for letter in word :
    key = list(letter.split())
    this_one.update({key[0]:key[1]})

for letter in s :
    sentence = sentence + this_one.get(letter,letter) + ' '
print(sentence)