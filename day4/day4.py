with open("day4/test.txt") as file:
    numbers = file.readline()
    # boards = file.read().splitlines()
    boards = file.readlines()

newboards = []
for line in boards:
    b = -1
    if line == '\n':
        newboards.append([])
        b += 1
    else:
        newboards[b].append(line)
print(numbers)

boards = newboards
for board in newboards:
    for line in range(len(board)):
        board[line] = board[line].rstrip()
        board[line] = list(map(int, board[line].split()))
        for i in range(len(board[line])):
            board[line][i] = [board[line][i], 'n']


