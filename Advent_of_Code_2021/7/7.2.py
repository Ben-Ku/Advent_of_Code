#!/usr/bin/python3
from utils import *
from runner import run, run_samples, get_commands
from collections import *
import sys
import time
import datetime
sys.path.extend(['..', '.'])
def get_day(): return datetime.date.today().day
def get_year(): return 2021


def p1(v):

    s = list(map(int, v.split(',')))
    s.sort()

    def cacluclate_cost_1(pos):
        cost = 0
        for i in s:
            n = abs(pos-i)
            cost += n
        return cost

    best_pos = 10**8
    for i in range(s[0], s[-1]+1):
        cost = cacluclate_cost_1(i)
        best_pos = min(best_pos, cost)

    print(best_pos)

    return best_pos


def p2(v):
    def cacluclate_cost1(pos):
        cost = 0
        for i in s:
            n = abs(pos-i)
            cost += n*(n+1)//2
        return cost
    return p1(v)


if __name__ == '__main__':
    cmds = [
        'run1', 'run2',
        # 'print_stats',
        'submit1',
        # 'submit2'
    ]
    print('Commands:', cmds)
    if 'run_samples' in cmds or 'samples_only' in cmds:
        run_samples(p1, p2, cmds, __file__)
    if 'samples_only' not in cmds:
        run(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
