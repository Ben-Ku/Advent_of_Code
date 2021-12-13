
with open('input8.1.txt') as file:
    s = file.read().split('\n')


s = [i.split('|') for i in s]


for i in range(len(s)):
    s[i] = [s[i][0].split(), s[i][1].split()]


def determine_numbers(case):
    case[0] = [''.join(i) for i in list(map(sorted, case[0]))]
    case[1] = [''.join(i) for i in list(map(sorted, case[1]))]

    dig = {}
    for digit in case[0]:
        if len(digit) == 2:
            dig[1] = set(digit)
        if len(digit) == 3:
            dig[7] = set(digit)
        if len(digit) == 4:
            dig[4] = set(digit)
        if len(digit) == 7:
            dig[8] = set(digit)

    mapped_to = {}
    mapped_to['a'] = dig[7].difference(dig[1])

    # find 0
    for digit in case[0]:
        if len(digit) == 6:
            if len(set(digit).intersection(dig[4].difference(dig[1]))) == 1:
                dig[0] = set(digit)

    # find 2
    for digit in case[0]:
        if len(digit) == 5:
            if len(set(digit).intersection(dig[4])) == 2:
                dig[2] = set(digit)

    # find 3
    for digit in case[0]:
        if len(digit) == 5:
            if len(set(digit).difference(dig[1])) == 3:
                dig[3] = set(digit)

    # find 5
    for digit in case[0]:
        if len(digit) == 5:
            if set(digit) != dig[2] and set(digit) != dig[3]:
                dig[5] = set(digit)

    # find 6
    for digit in case[0]:
        if len(digit) == 6:
            if len(set(digit).intersection(dig[1])) == 1:
                dig[6] = set(digit)

    # find 9
    for digit in case[0]:
        if len(digit) == 6:
            if set(digit) != dig[0] and set(digit) != dig[6]:
                dig[9] = set(digit)

    dig_list = {}
    for i in range(10):
        st = ''.join(sorted(list(dig[i])))
        if i == 2:
            dig_list[st] = 2
        dig_list[st] = i

    res = ''
    for digit in case[1]:

        res += str(dig_list[digit])

    return int(res)


res = 0
for case in s:
    res += determine_numbers(case)

print(res)
