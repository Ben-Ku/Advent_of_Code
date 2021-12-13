
with open('input1.1.txt') as file:
    s = file.read()

    passports = s.split('\n\n')

keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  # 'cid' excluded

res = 0
for passport in passports:
    valid = True
    for key in keys:
        if key not in passport:
            valid = False
            break
    if valid:
        res += 1
print(res)
