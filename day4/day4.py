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

numbers = numbers.strip()
numbers = list(map(int, numbers.split(',')))

boards = newboards
for board in newboards:
    for line in range(len(board)):
        board[line] = board[line].rstrip()
        board[line] = list(map(int, board[line].split()))
        for i in range(len(board[line])):
            board[line][i] = [board[line][i], 'n']


for number in numbers:
    for board in boards:
        for line in board:
            for num in line:
                if num[0] == number:
                    num[1] = 'y'

    checkBingo(boards)

def checkBingo(boards):
    horizontalBingo = False
    verticalBingo = False
    for board in boards:
        for line in board:
            
            for num in line:
                if num[1] == 'n': 
                    