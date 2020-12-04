file = open("Day-1/input.txt")
input = file.read().splitlines()
input = [int(k) for k in input]


answer = 0
for i in input:
    for j in input:
        if i != j and i + j == 2020:
            answer = i * j

print(answer)
