import math

file = open("Day-5/input.txt")
input = file.read().splitlines()


def front(interval):
    return [interval[0], math.floor((interval[0] + interval[1]) / 2)]


def back(interval):
    return [math.ceil((interval[0] + interval[1]) / 2), interval[1]]


all_seatID = []

for i in input:
    row_interval = [0, 127]
    for j in i[:-3]:
        if j == "F":
            row_interval = front(row_interval)
        if j == "B":
            row_interval = back(row_interval)
    row = row_interval[0]

    col_interval = [0, 7]
    for j in i[-3:]:
        if j == "L":
            col_interval = front(col_interval)
        if j == "R":
            col_interval = back(col_interval)
    col = col_interval[0]

    seatID = row * 8 + col
    all_seatID.append(seatID)

all_seatID.sort()

my_seat = 0
for i in all_seatID:
    my_seat = i + 1
    if not my_seat in all_seatID:
        break
print(my_seat)
