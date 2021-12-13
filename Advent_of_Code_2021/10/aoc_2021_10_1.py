
# with open('input9.1.txt') as file:
with open('input10.1.txt') as file:
    s = file.read().split('\n')

for i in range(1000):
    s = [''.join(i.split('[]')) for i in s]
    s = [''.join(i.split('{}')) for i in s]
    s = [''.join(i.split('()')) for i in s]
    s = [''.join(i.split('<>')) for i in s]
k = s.copy()

res = 0
not_corrupted = []
for j, st in enumerate(s):
    corrupted = False
    for i in st:
        if i == ')':
            res += 3
            corrupted = True
            break
        if i == ']':
            res += 57
            corrupted = True
            break
        if i == '}':
            res += 1197
            corrupted = True
            break
        if i == '>':
            res += 25137
            corrupted = True
            break
    if not corrupted:
        not_corrupted.append(j)

print(res)
for i in s:
    print(i)
print(not_corrupted)

points = {}
points['('] = 1
points['['] = 2
points['{'] = 3
points['<'] = 4

scores = []

for i in not_corrupted:
    st = s[i][::-1]
    current_score = 0

    for j in st:
        current_score *= 5
        current_score += points[j]
    scores.append(current_score)
scores.sort()

res = scores[len(scores)//2]
print(res)
