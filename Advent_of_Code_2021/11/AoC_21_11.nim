import strutils
import sequtils
import tables


var
    s = readFile("input11.1.txt")
    s_list = s.split("\n")
    grid: seq[seq[int]]

for line in s_list:
    grid.add(line.mapIt(parseInt($it)))

type Point = tuple
    x: int
    y: int

var gonna_flash: seq[Point]

for r, row in grid:
    for c, element in row:
        if element == 9:
            gonna_flash.add((r, c))

var has_flashed = 0
bfs = []


#[ for row in grid:
    echo row
]#
