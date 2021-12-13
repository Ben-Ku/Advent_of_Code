
with open('input2.1.txt') as file:
    s = file.read().split('\n')


def get_rates(s):
    rates = [0]*len(s[0])

    for bi in s:
        for i in range(len(bi)):
            if bi[i] == '0':
                rates[i] += 1

    num1 = ''
    num2 = ''
    for rate in rates:
        if rate > len(s)//2:
            num1 += '0'
            num2 += '1'
        else:
            num2 += '0'
            num1 += '1'

    return num1, num2


num1, num2 = get_rates(s)


def find_ox(s, n=0):
    if len(s) == 1 or n == len(s[0]):
        return s[0]
    else:
        num1, num2 = get_rates(s)
        new_s = []
        for bi in s:
            if bi[n] == num1[n]:
                new_s.append(bi)
        return find_ox(new_s, n+1)


def find_co(s, n=0):
    if len(s) == 1 or n == len(s[0]):
        return s[0]
    else:
        num1, num2 = get_rates(s)
        new_s = []
        for bi in s:
            if bi[n] == num2[n]:
                new_s.append(bi)
        return find_co(new_s, n+1)


print(num1, find_ox(s))
print(num2, find_co(s))

ox = int(find_ox(s), 2)
co = int(find_co(s), 2)

print(ox, co)

print(int(find_co(s), 2) * int(find_ox(s), 2))
