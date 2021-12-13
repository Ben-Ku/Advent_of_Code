from collections import Counter

c = Counter()

c['potato'] += 1

print(c)
c[''] = 9
c['abc'] += 7
print(c.most_common(3))

d = Counter(['potato'])

c.update(d)
print(c)
