

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
    for pair, ammount in pairs.items():
        middle = h[pair]
        p1 = pair[0] + middle 
        p2 = middle + pair[1]
        if middle in count:
            count[middle] += ammount
        else:
            count[middle] = ammount
        for pair in (p1,p2):
            if pair in h:
                if pair in new_pairs:
                    new_pairs[pair] += ammount
                else:
                    new_pairs[pair] = ammount
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
