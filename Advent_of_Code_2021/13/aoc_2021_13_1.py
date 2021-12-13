

from os import closerange


print('\n'*20)

with open('input13.1.txt') as file:
    # with open('test.txt') as file:
    # with open('test.txt') as file:
    s = file.read().split('\n\n')


dots, instructions = s[0], s[1]
dots = dots.split('\n')
instructions = instructions.split('\n')

dots = [[int(j) for j in i.split(',')] for i in dots]
instructions = [i.split(' ')[2] for i in instructions]
instructions = [[i[0], int(i[2:])] for i in instructions]


width = max([i[0]+1 for i in dots])
height = max([i[1]+1 for i in dots])


grid = [['.' for _ in range(width)] for _ in range(height)]

for dot in dots:
    x, y = dot

    grid[y][x] = '#'


def pr():
    for row in grid:
        print(''.join([str(i) for i in row]))
    print()


for ins in instructions:
    di = ins[0]
    num = ins[1]
    print(di)
    if di == 'y':
        for r in range(1, min(height-num, num+1)):
            for x in range(width):
                if grid[num-r][x] == '#' or grid[num+r][x] == '#':
                    grid[num-r][x] = '#'
        grid = grid[:num]
    else:
        for c in range(1, min(width-num, num+1)):
            for y in range(height):
                try:
                    if grid[y][num-c] == '#' or grid[y][num+c] == '#':
                        grid[y][num-c] = '#'
                except:
                    print(num+c,)
                    exit()

        grid = [row[:num] for row in grid]

    width = len(grid[0])
    height = len(grid)


pr()

res = 0
for row in grid:
    for e in row:
        if e == '#':
            res += 1

print(res)
