# a football team plays 30 game, getting score of each game, printing sum of scores and the number of games the team wins
count = 0
sum = 0
for i in range (30) :
    x = int (input())

    if x == 3 :
        count += 1
        sum = sum + 3
    elif x == 1 :
        sum = sum + 1

print ( sum , count)
