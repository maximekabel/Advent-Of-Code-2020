file = open("Day-6/input.txt")
input = file.read().split("\n\n")


yess = []

for i in input:
    yess.append(len(set(i.replace("\n", ""))))

print(sum(yess))