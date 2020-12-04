file = open("Day-2/input.txt")
input = file.read().splitlines()

correct_passw = 0

test_list = []
for i in input:
    lower_lim = int(i.split("-", 1)[0])
    upper_lim = int(i.split("-")[1].split(" ")[0])
    char = i.split("-")[1].split(" ")[1].rstrip(":")
    password = i.split(":")[1].strip()
    dic = {"lower": lower_lim, "upper": upper_lim, "char": char, "password": password}
    test_list.append(dic)


for k in test_list:
    occurance = k["password"].count(k["char"])
    if occurance >= k["lower"] and occurance <= k["upper"]:
        correct_passw += 1

print(correct_passw)
