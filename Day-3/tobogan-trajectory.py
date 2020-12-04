file = open("Day-3/input.txt")
input = file.read().splitlines()

longitude = 0
tree_count = 0

for i in input:
    # print(i[longitude])
    if i[longitude] == "#":
        tree_count += 1

    longitude += 3

    if longitude > (len(i) - 1):
        longitude = longitude - len(i)
    # print(longitude)
print(tree_count)
