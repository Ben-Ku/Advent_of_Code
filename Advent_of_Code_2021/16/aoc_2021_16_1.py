

print('\n'*20)

with open('input16.1.txt') as file:
    # with open('test.txt') as file:
    s = file.read().rstrip()

he = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

# s = 'D2FE28'
# s = 'EE00D40C823060'
# s = """A0016C880162017C3686B18A3D4780"""


# while s[0] == '0':
#     s = s[1:]

# s = '001 001 1 00000000011 '
# s1 = '100 100 00001'
# s2 = '100 100 00011'
# s3 = '001 001 0 000000000100001    100 100 00011     100 100 00011      100 100 00011'
# s = s + s1 + s2 + s3

s = s.replace(' ', '')


def parse_num(s):
    print('Parsing int')
    num = ''
    while s[0] == '1':
        num += s[1:5]
        s = s[5:]
    num += s[1:5]
    s = s[5:]
    num = int(num, 2)
    return s, num


def type_id_thing(package_id, values):
    if len(values) == 1:
        return values[0]
    if package_id == 0:
        res = sum(values)
    # product
    elif package_id == 1:
        res = values[0]
        for value in values[1:]:
            res *= value
    # minimum
    elif package_id == 2:
        res = min(values)
    # maximum
    elif package_id == 3:
        res = max(values)
    elif package_id == 4:
        res = values[0]
    # greater than
    elif package_id == 5:
        res = int(values[0] > values[1])
    # less than
    elif package_id == 6:
        res = int(values[0] < values[1])
    # equal to
    elif package_id == 7:
        res = int(values[0] == values[1])

    return res


versum = 0


def parse_s(s, parse_limit=10**10, T=-1):
    global versum
    parsed = 0
    values = []
    V = int(s[0:3], 2)
    if T == -1:
        T = int(s[3:6], 2)
    while parsed <= parse_limit and s != '':
        if len(s) > 0:
            if int(s, 2) == 0:
                break
        v = int(s[0:3], 2)

        t = int(s[3:6], 2)
        s = s[6:]
        versum += v
        print(f'Ver: {v} ID: {t} VERSUM: {versum}:')
        if t == 4:
            while s[0:3] == '00':
                s = s[1:]
            s, value = parse_num(s)
            print(f'NUMBER: {value}')
        else:
            i = int(s[0])
            s = s[1:]
            if i == 0:
                l = int(s[:15], 2)  # total length of sub-packets
                print(f'parsing subpackages of length {l}')
                s = s[15:]
                sub_s = s[:l]
                meh, value = parse_s(sub_s, 10**10, T)
                s = s[l:]
            else:
                l = int(s[:11], 2)  # numer of sub-packets
                print(f'parsing {l} subpackages')
                s = s[11:]
                nu_of_s = s[:l]
                s, value = parse_s(s, parse_limit, T)
        parsed += 1
        values.append(value)
        print('------------------------------------------------------------')

    print(f'Values: {values} ID : {T}')

    print('OMG')
    value = type_id_thing(T, values)
    print('wtf why no end')

    return s, value


def main():
    s = 'C200B40A82'
    s = ''.join([he[i] for i in s])
    s, value = parse_s(s)
    print(f'versum: {versum} Value: {value}')


if __name__ == "__main__":
    main()
