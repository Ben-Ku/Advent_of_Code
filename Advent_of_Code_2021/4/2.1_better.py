
with open('input2.1.txt') as file:
    s = file.read().split('\n\n')


order = list(map(int, s[0].split(',')))

b = []
for board in s[1:]:
    b.append(([list(map(int, i)) for i in [i.split()
             for i in board.split('\n')]]))
l = len(b)

b_position = [dict() for _ in range(l)]
b_r = [dict() for _ in range(l)]
b_c = [dict() for _ in range(l)]
for i in range(l):
    for r in range(5):
        for c in range(5):
            board = b[i]
            b_position[i][board[r][c]] = (r, c)
            b_r[i][r] = 0
            b_c[i][c] = 0


def get_score(board_index):
    score = 0
    for r in range(5):
        for c in range(5):
            if (r, c) not in marked[i]:
                score += b[board_index][r][c]
                print(score)

    return score


marked = [dict() for _ in range(l)]
good_boards = []
scores = dict()
for j, o in enumerate(order):
    for i in range(l):
        if o in b_position[i]:
            r, c = b_position[i][o]
            marked[i][(r, c)] = True
            b_r[i][r] += 1
            b_c[i][c] += 1
            if b_r[i][r] == 5 or b_c[i][c] == 5 and i not in good_boards:
                good_boards.append(i)
                scores[i] = get_score(i) * j

print(scores)
first_index = good_boards[0]
last_index = good_boards[-1]
print(get_score(first_index))
print(first_index, last_index)
print(scores[first_index], scores[last_index])
