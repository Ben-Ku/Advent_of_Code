

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

print(p)
print(t)


for j in range(40):
    newp = p[0]
    for i in range(len(p)-1):
        st = p[i:i+2]
        if st in h:
            newp += h[st]
        newp += st[1]
    print(j)
    p = newp

count = {}
for c in newp:

    if c in count:
        count[c] += 1
    else:
        count[c] = 1

smallest = 10**10
largest = 0

for c in count.values():
    largest = max(c, largest)
    smallest = min(c, smallest)

print(largest-smallest)
