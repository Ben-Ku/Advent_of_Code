
with open('input1.1.txt') as file:
    s = [int(i[:-1]) for i in file.readlines()]

count = 0
for i in range(1, len(s)):
    if s[i] > s[i-1]:
        count += 1


print(count)
