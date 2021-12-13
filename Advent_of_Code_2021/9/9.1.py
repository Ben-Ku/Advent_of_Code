
# with open('input9.1.txt') as file:
with open('test.txt') as file:
    s = file.read().split('\n')

s = [list(map(int, list(row))) for row in s]

w = len(s[0])
h = len(s)
res = 0
for r in range(len(s)):
    for c in range(len(s[0])):
        num = s[r][c]
        if c < w-1:
            if not num < s[r][c+1]:
                continue
        if r < h-1:
            if not num < s[r+1][c]:
                continue
        if c > 0:
            if not s[r][c] < s[r][c-1]:
                continue
        if r > 0:
            if not s[r][c] < s[r-1][c]:
                continue

        res += s[r][c] + 1
        print(r, c, num)

s = [[9, *row, 9] for row in s]
s = [[9]*len(s[0]), *s, [9]*len(s[0])]

for row in s:
    print(row)
print(res)
