file = open("Day-3/input.txt")
input = file.read().splitlines()

longitude = 0

# tree count for 1 right
tree_count_1 = 0
for i in input:
    # print(i[longitude])
    if i[longitude] == "#":
        tree_count_1 += 1

    longitude += 1

    if longitude > (len(i) - 1):
        longitude = longitude - len(i)
    # print(longitude)

# tree count for 3 right
tree_count_3 = 0
longitude = 0
for i in input:
    # print(i[longitude])
    if i[longitude] == "#":
        tree_count_3 += 1

    longitude += 3

    if longitude > (len(i) - 1):
        longitude = longitude - len(i)
    # print(longitude)

# tree count for 5 right
tree_count_5 = 0
longitude = 0
for i in input:
    # print(i[longitude])
    if i[longitude] == "#":
        tree_count_5 += 1

    longitude += 5

    if longitude > (len(i) - 1):
        longitude = longitude - len(i)
    # print(longitude)

# tree count for 7 right
tree_count_7 = 0
longitude = 0
for i in input:
    # print(i[longitude])
    if i[longitude] == "#":
        tree_count_7 += 1

    longitude += 7

    if longitude > (len(i) - 1):
        longitude = longitude - len(i)
    # print(longitude)

other_input = input[::2]
tree_count_2_1 = 0
longitude = 0
for i in other_input:
    # print(i[longitude])
    if i[longitude] == "#":
        tree_count_2_1 += 1

    longitude += 1

    if longitude > (len(i) - 1):
        longitude = longitude - len(i)
    # print(longitude)

print(tree_count_1)
print(tree_count_3)
print(tree_count_5)
print(tree_count_7)
print(tree_count_2_1)

output = tree_count_1 * tree_count_3 * tree_count_5 * tree_count_7 * tree_count_2_1
print(output)
