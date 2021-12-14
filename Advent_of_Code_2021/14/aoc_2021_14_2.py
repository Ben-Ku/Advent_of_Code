

print('\n'*20)

with open('input14.1.txt') as file:
    # with open('test.txt') as file:
    s = file.read().split('\n\n')

t = s[1].split('\n')
t = [i.split(' -> ') for i in t]
p = s[0]


h = {}
for a, b in t:
    h[a] = b

count = {}
for c in p:
    if c in count:
        count[c] += 1
    else:
        count[c] = 1


def insert(pairs):
    new_pairs = {}
    for pair in pairs.keys():
        nbr = pairs[pair]
        middle = h[pair]
        pair = pair[0] + middle + pair[1]
        if middle in count:
            count[middle] += nbr
        else:
            count[middle] = nbr
        p1 = pair[0:2]
        p2 = pair[1:3]
        if p1 in h:
            if p1 in new_pairs:
                new_pairs[p1] += nbr
            else:
                new_pairs[p1] = nbr
        if p2 in h:
            if p2 in new_pairs:
                new_pairs[p2] += nbr
            else:
                new_pairs[p2] = nbr
    return new_pairs


pairs = {}
for i in range(len(p)-1):
    st = p[i:i+2]
    if st in h:
        if st in pairs:
            pairs[st] += 1
        else:
            pairs[st] = 1


for i in range(40):
    pairs = insert(pairs)


largest = max(count.values())
smallest = min(count.values())

print(largest-smallest)
print(count)
