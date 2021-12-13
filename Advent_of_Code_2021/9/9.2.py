
with open('input9.1.txt') as file:
    # with open('test.txt') as file:
    s = file.read().split('\n')

s = [list(map(int, list(row))) for row in s]

w = len(s[0])
h = len(s)
low_points = []
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

        low_points.append((r+1, c+1))


s = [[9, *row, 9] for row in s]
s.insert(0, [9]*len(s[0]))
s.append([9]*len(s[0]))

w = len(s[0])
h = len(s)

visited = {}
basins = []
while low_points:
    dfs = [low_points.pop()]
    (r, c) = dfs[0]
    if (r, c) in visited:
        continue
    else:
        visited[r, c] = True
        basin_size = 1
    while dfs:
        r, c = dfs.pop()
        new_locs = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
        for nr, nc in new_locs:
            if (nr, nc) not in visited and s[nr][nc] != 9:
                dfs.append((nr, nc))
                visited[nr, nc] = True
                basin_size += 1
                s[nr][nc] = '.'
    basins.append(basin_size)

for (r, c) in visited.keys():
    if s[r][c] != '.':
        s[r][c] = '#'

for row in s:
    row = list(map(str, row))
    print(''.join(row))

basins.sort()

res = basins[-1]*basins[-2]*basins[-3]
print(res)
