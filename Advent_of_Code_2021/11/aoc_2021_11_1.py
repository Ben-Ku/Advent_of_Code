
with open('input11.1.txt') as file:
    # with open('test.txt') as file:
    s = file.read().split('\n')
    s = [list(map(int, list(i))) for i in s]

border = {}
s = [[0, *i, 0] for i in s]
s.insert(0, 12*[0])
s.append(12*[0])

di = ([1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1])


def new_step(s):
    visited = {}
    flashed = []
    for i in range(12):
        border[0, i] = True
        border[11, i] = True
        border[i, 0] = True
        border[i, 11] = True
    for r in range(1, 11):
        for c in range(1, 11):
            s[r][c] += 1
            if s[r][c] == 10:
                flashed.append((r, c))
                visited[r, c] = True

    count = 0
    while flashed:
        r, c = flashed.pop()
        visited[r, c] = True
        count += 1
        for dr, dc in di:
            nr, nc = r+dr, c+dc
            if (nr, nc) in border:
                continue
            s[nr][nc] += 1
            if (nr, nc) in visited:
                continue
            if s[r+dr][c+dc] >= 10 and (r+dr, c+dc) not in visited:
                flashed.append((r+dr, c+dc))
                s[nr][nc] = 0
                visited[(r+dr, c+dc)] = True
    for r, c in visited:
        s[r][c] = 0

    if len(visited) == 100:
        count = 'allah'

    return s, count


res = 0
print('\n'*100)
for j in range(500):

    s, count = new_step(s)
    if count == 'allah':
        print(j+1)
        print('mhmd')
        break
    res += count
