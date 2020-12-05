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
    if (
        ("byr" in i)
        and ("iyr" in i)
        and ("eyr" in i)
        and ("hgt" in i)
        and ("hcl" in i)
        and ("ecl" in i)
        and ("pid" in i)
    ):
        valid_passport += 1
print(valid_passport)
