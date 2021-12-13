
with open('input1.1.txt') as file:
    s = [int(i[:-1]) for i in file.readlines()]

count = 1
for i in range(3, len(s)):
    if s[i] > s[i-3]:
        count += 1

print(count)
