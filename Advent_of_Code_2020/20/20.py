from pprint import pprint
import re
l = 10

tiles = {}
index = 0


def process_side(side):
    return ''.join(['0' if s == '.' else '1' for s in side])


tiles_that_have_side: dict[set] = {}


with open("input_e.txt") as file:
    for block in re.split(r"^$", file.read().strip(), flags=re.MULTILINE):
        lines = block.strip().split("\n")

        tile_id = int(lines[0].split(" ")[1][:-1])

        top = process_side(lines[1])
        bottom = process_side(lines[-1])
        left = process_side(''.join([lines[i][0]
                            for i in range(1, l+1)]))
        right = process_side(''.join([lines[i][-1]
                                      for i in range(1, l+1)]))

        #print(tile_id, top, right, bottom, left)
        tiles[tile_id] = (top, right, bottom, left)

        for side in [top, right, bottom, left] + [top[::-1], right[::-1], bottom[::-1], left[::-1]]:
            if side in tiles_that_have_side:
                tiles_that_have_side[side].add(tile_id)
            else:
                tiles_that_have_side[side] = set([tile_id])

# pprint(tiles_that_have_side)


def add_edge(graph, node1, node2):
    if node1 in graph:
        graph[node1].add(node2)
    else:
        graph[node1] = set([node2])

    if node2 in graph:
        graph[node2].add(node1)
    else:
        graph[node2] = set([node1])


graph = {}
for tile_ids in tiles_that_have_side.values():
    if len(tile_ids) > 1:
        node1 = tile_ids.pop()
        node2 = tile_ids.pop()

        add_edge(graph, node1, node2)

corners = []
for key, value in graph.items():
    if len(value) == 2:
        corners.append(key)

result = 1
for key in corners:
    result *= key

print(result)  # 20899048083289


def main():
    ...



"""
0: 1 3
1: "a"
2: "b"
3: 1 | 0

0 => ^(aaa(aaa|bb))$

yacc

https://github.com/scholvin/aoc-2020/blob/main/src/make-bison.awk

https://en.wikipedia.org/wiki/GNU_Bison


0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"

^((a)((ab)|(ba)))$

aabbab

"""


# Example 1: 20899048083289

if __name__ == "__main__":
    main()
