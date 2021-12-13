
with open('input5.1.txt') as file:
    s = file.read().split('\n')

r""

s = [list(map(int, i.replace('->', '').replace(',', ' ').split())) for i in s]
# 911, 808 -> 324, 221

count = 0
visited = dict()
for p in s:
    x, y, a, b = p
    if x == a:
        if y > b:
            y, b = b, y
        for i in range(y, b+1):
            if (x, i) in visited:
                if visited[x, i] == 1:
                    count += 1
                    visited[x, i] = 2
            else:
                visited[x, i] = 1
    elif y == b:
        if x > a:
            x, a = a, x
        for i in range(x, a+1):
            if (i, y) in visited:
                if visited[i, y] == 1:
                    count += 1
                    visited[i, y] = 2
            else:
                visited[i, y] = 1
    else:
        if x > a:
            x, y, a, b = a, b, x, y
        for i in range(a+1-x):
            if b > y:
                dx, dy = x+i, y+i
            else:
                dx, dy = x+i, y-i
            print(dx, dy)
            if (dx, dy) in visited:
                if visited[dx, dy] == 1:
                    count += 1
                    visited[dx, dy] = 2
            else:
                visited[dx, dy] = 1

for r in range(10):
    line = [0 for _ in range(10)]
    for c in range(10):
        if (r, c) in visited:
            line[c] = visited[r, c]
        line = list(map(str, line))
    print(''.join(line))


print(count)
