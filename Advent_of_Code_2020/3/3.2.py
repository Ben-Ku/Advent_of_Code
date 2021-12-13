import re

grid = []
with open('input3.1.txt') as file:
    grid = file.read().splitlines()


height = len(grid)
width = len(grid[0])

print(grid)

result = 1
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for dy, dx in slopes:
    y = 0
    trees = 0
    for x in range(0, height, dx):
        if grid[x][y] == '#':
            trees += 1
        y += dy
        y %= width
    print(trees)
    result *= trees

print(result)
