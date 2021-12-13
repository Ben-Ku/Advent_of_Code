import re

regex = r"(\d+)-(\d+) (\w): (\w+)"
with open('input1.txt') as file:
    s = file.read()
    matches = re.findall(regex, s)

valid_passwords = 0
for match in matches:
    a = int(match[0])-1
    b = int(match[1])-1
    letter = match[2]
    word = match[3]

    if (word[a] == letter and word[b] != letter) or (word[a] != letter and word[b] == letter):
        valid_passwords += 1

print(valid_passwords)
