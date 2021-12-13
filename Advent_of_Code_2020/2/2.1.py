import re

regex = r"(\d+)-(\d+) (\w): (\w+)"
with open('input1.txt') as file:
    s = file.read()
    matches = re.findall(regex, s)

valid_passwords = 0
for match in matches:
    lo = int(match[0])
    hi = int(match[1])
    letter = match[2]
    word = match[3]
    ammount = word.count(letter)
    if lo <= ammount <= hi:
        valid_passwords += 1

print(valid_passwords)
