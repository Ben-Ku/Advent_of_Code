import heapq
from collections import deque
from collections import Counter
from collections import defaultdict

print('\n'*20)

with open('input12.1.txt') as file:
    # with open('test.txt') as file:
    # with open('test.txt') as file:
    s = file.read().split('\n')


s = [i.split('-') for i in s]

graph = {}
for pair in s:
    a, b = pair
    if a in graph:
        graph[a].add(b)
    else:
        graph[a] = {b}

    if b in graph:
        graph[b].add(a)
    else:
        graph[b] = {a}


def find_paths(graph, current_path=[], count=0, visited={}):
    if len(current_path) == 0:
        current_path.append('start')
        visited['start'] = True
    node = current_path[-1]

    count = 0
    for nbr in graph[node]:
        if nbr in visited:
            continue
        else:

            if nbr.lower() == nbr:
                visited(nbr)


dfs = [['start']]
count = 0
paths = []

while dfs:
    path = dfs.pop()
    node = path[-1]
    for nbr in graph[node]:
        new_path = path.copy()
        if nbr == 'end':
            paths.append([*new_path, 'end'])
            count += 1
            continue
        if nbr.lower() not in new_path:
            new_path.append(nbr)
            dfs.append(new_path)

for path in paths:
    print(' '.join(path))
print(count)


