# n is the nember of player and l like this inputs  5 6 1 3 is how many times they played in matches. How many teams we can arrange with players who played maximum 2 times. 3 player in a team.
space_split = []
n = int(input())
l = input()
space_split = l.split()
space_split = list(map(int,space_split))
space_split.sort()
for letter in reversed(space_split) :
    if letter >= 3 :
        space_split.pop()
i = len(space_split)
i = int(i / 3)
print(i)
