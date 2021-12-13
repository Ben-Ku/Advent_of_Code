
with open('input2.1.txt') as file:
    s = file.read().split('\n\n')

order = s[0]

b = []
for board in s[1:]:
    b.append(([list(map(int, i)) for i in [i.split()
             for i in board.split('\n')]]))


def check_bingo(board, num):
    for row in range(0, 5):
        for col in range(0, 5):
            if board[row][col] == num:

                board[row][col] = -1
                for i in range(0, 5):
                    if board[i][col] != -1:
                        for j in range(0, 5):
                            if board[row][j] != -1:
                                return board, False
                        return board, True
                return board, True
    return board, False


def score(board):
    count = 0
    for row in board:
        for num in row:
            if num == -1:
                count += 1
    return sum(sum(i) for i in board) + count


bo = [[66, 78, 7, 45, 92], [39, 38, 62, 81, 77], [
    9, 73, 25, 97, 99], [87, 80, 19, 1, 71], [85, 35, 52, 26, 68]]

print(check_bingo(bo, 66))
order = [int(i) for i in order.split(',')]


done = {}
for count in range(len(order)):
    for i in range(len(b)):
        num = order[count]
        b[i], val = check_bingo(b[i], num)

        # print(check_bingo(b[0], 66))
        if i == 0:
            print(b[0], order[count], val)

        if val == True and i not in done:
            done[i] = True
            last_score = score(b[i])*num

print(last_score)
