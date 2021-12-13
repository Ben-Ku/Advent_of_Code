s = input()

cups = {}
cups[1] = 1
cups[2] = 0
cups[3] = 0

for move in s:
    if move == 'A':
        cups[1], cups[2] = cups[2], cups[1]
    if move == 'B':
        cups[2], cups[3] = cups[3], cups[2]
    if move == 'C':
        cups[1], cups[3] = cups[3], cups[1]

for i in range(1, 4):
    if cups[i] == 1:
        print(i)
