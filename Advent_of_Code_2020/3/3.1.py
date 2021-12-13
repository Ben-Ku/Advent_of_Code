import re

grid = []
with open('input3.1.txt') as file:
    grid = file.read().splitlines()



height = len(grid)
width = len(grid[0])

trees = 0
slope = 3
index = 0
for i in range(height):
    if grid[i][index] == '#':
        trees += 1
    index += slope
    index %= width

print(trees)
