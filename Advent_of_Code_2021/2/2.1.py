
with open('input2.1.txt') as file:
    s = file.read().split('\n')
    print(s)

print(s)
hor = 0
ver = 0
aim = 0
for direction in s:
    d, val = direction.split()
    val = int(val)
    if d == 'forward':
        hor += val
        ver += aim*val
    if d == 'down':
        aim += val
    if d == 'up':
        aim -= val


print(s)

print(hor*ver)
