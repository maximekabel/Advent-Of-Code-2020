file = open("Day-1/input.txt")
input = file.read().splitlines()
input = [int(k) for k in input]


answer = 0
for i in input:
    for j in input:
        if i != j and i + j == 2020:
            answer = i * j

answer_pt_2 = 0
for m in input:
    for n in input:
        for l in input:
            if m != n != l and m + n + l == 2020:
                answer_pt_2 = m * n * l

print("Answer Part 1:" + str(answer))
print("Answer Part 2:" + str(answer_pt_2))
