file = open("Day-4/input.txt")
input = file.read().split("\n\n")

valid_passport = 0
passports = []
for b in input:
    dic = {}
    passp = b.replace("\n", " ").rstrip().split(" ")
    for i in passp:
        a = i.split(":")
        dic[a[0]] = a[1]

    passports.append(dic)

for i in passports:
    valid = True
    if not ("byr" in i) or not (1920 <= int(i["byr"]) <= 2002):
        valid = False
    if not ("iyr" in i) or not (2010 <= int(i["iyr"]) <= 2020):
        valid = False
    if not ("eyr" in i) or not (2020 <= int(i["eyr"]) <= 2030):
        valid = False
    if not ("hgt" in i):
        valid = False
    if "hgt" in i:
        if i["hgt"].endswith("cm"):
            if not (150 <= int(i["hgt"][:-2]) <= 193):
                valid = False
        elif i["hgt"].endswith("in"):
            if not (59 <= int(i["hgt"][:-2]) <= 76):
                valid = False
        else:
            valid = False
    if (
        not ("hcl" in i)
        or (i["hcl"][0] != "#")
        or any([a not in "0123456789abcdef" for a in i["hcl"][1:]])
    ):
        valid = False
    if not ("ecl" in i) or i["ecl"] not in [
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth",
    ]:
        valid = False
    if not ("pid" in i) or len(i["pid"]) != 9 or not i["pid"].isdigit():
        valid = False

    if valid:
        valid_passport += 1
print(valid_passport)
