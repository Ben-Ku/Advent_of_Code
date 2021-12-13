with open('input7.1.txt') as file:
    s = list(map(int, file.read().split(',')))


s.sort()


def cacluclate_cost(pos):
    cost = 0
    for i in s:
        n = abs(pos-i)
        cost += n*(n+1)//2
    return cost


best_pos = 10**8
for i in range(s[0], s[-1]+1):
    cost = cacluclate_cost(i)
    best_pos = min(best_pos, cost)


print(best_pos)
