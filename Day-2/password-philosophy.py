file = open("Day-2/input.txt")
input = file.read().splitlines()

correct_passw1 = 0
correct_passw2 = 0

test_list = []
for i in input:
    lower_lim = int(i.split("-", 1)[0])
    upper_lim = int(i.split("-")[1].split(" ")[0])
    char = i.split("-")[1].split(" ")[1].rstrip(":")
    password = i.split(":")[1].strip()
    dic = {"lower": lower_lim, "upper": upper_lim, "char": char, "password": password}
    test_list.append(dic)


for m in test_list:
    occurance = m["password"].count(m["char"])
    if occurance >= m["lower"] and occurance <= m["upper"]:
        correct_passw1 += 1

for k in test_list:

    char_pos_a = k["password"][k["lower"] - 1]
    char_pos_b = k["password"][k["upper"] - 1]

    if (char_pos_a == k["char"] and char_pos_b != k["char"]) or (
        char_pos_a != k["char"] and char_pos_b == k["char"]
    ):
        correct_passw2 += 1

print(correct_passw1)
print(correct_passw2)
