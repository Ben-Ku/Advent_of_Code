import re

with open('input1.1.txt') as file:
    s = file.read()

    passports = s.split('\n\n')


def lazy_int(l):
    for i in range(len(l)):
        try:
            if l[0] != '0':
                l[i] = int(l[i])
        except:
            continue
    return l


def is_valid(passport):
    p = passport.split()
    if len(p) < 7:
        return False
    p = [lazy_int(s.split(':')) for s in p]

    valid = True
    for key, val in p:
        if  key == 'byr' :
            if type(val) == int:
                if 1920 <= val <= 2002:
                    continue
        if  key == 'iyr' :
            if type(val) == int:
                if 2010 <= val <= 2020:
                    continue
        if  key == 'eyr' :
            if type(val) == int:
                if 2020 <= val <= 2030:
                    continue
        if  key == 'hgt':
            try:
                if key[-2:] == 'cm':
                    if 150 <= int(key[:-2]) <= 193:
                        continue
                elif key[-2:] == 'in':
                    if 59 <= <= 76:
            except:
                valid = False
                continue
        if  key == 'hcl' :
            if re.match(r'=?#[0-9a-f]{6}', val):
                continue
        if  key == 'ecl' :
            if val in 'amb blu brn gry grn hzl oth'.split():
                continue
        if  key == 'pid':
            if len(val) == 9:
                try:
                    int(val)
                    continue
                except:
                    continue
        return False

res = 0
for passport in passports:
    22



print(p)
