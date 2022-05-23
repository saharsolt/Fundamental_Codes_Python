# Getting a number as the number of votes, then getting the name of the country in the number of entries, storing in an array, and ordering it. Then, Count votes in an election for each country.
import collections

n = int(input())
country = []

for i in range(n):
    country.append(input())
counter = collections.OrderedDict()

for letter in country:
    if letter in counter:
        counter[letter] += 1
    else:
        counter[letter] = 1

for this_one in list(sorted(counter.keys())):
    print(this_one, counter[this_one])
