file = open("Day-6/input.txt")
input = file.read().split("\n\n")


yess = []

for i in input:
    first = []
    for j in i.rstrip("\n").split("\n"):
        new_first = []
        if not first:
            first = list(set(j))
        else:
            for k in set(j):
                if k in first:
                    new_first.append(k)
            first = new_first
            if not first:
                break

    yess.append(len(first))

print(sum(yess))