#input : 1+1+3+1+3
#output: 1+1+1+3+3
string = input()
string = string.replace('+', "")
y = ""
for i in range(len(string)):
    Min = 9
    for j in range(len(string)):
        if string[j] != " ":
            if int(string[j]) <= Min:
                Min = int(string[j])
                index = j
    y = y + str(Min) + '+'
    string = string[: index] + " " + string[index + 1:]
y = y[:-1]
print(y)