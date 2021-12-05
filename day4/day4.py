import pydash

def checkBingo(board):
    # check vertical bingo
    for col in range(5):
        i = 0
        for line in board:
            if line[col][1] == 'y':
                i += 1
            if i == 5:
                return False
    # check horizontal bingo
    for line in board:
        i = 0
        for num in line:
            if num[1] == 'y': 
                i += 1
            if i == 5:
                return True
    return False


with open("day4/input.txt") as file:
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

boom_pow = 0
currentBoard = 0
for number in numbers:
    for board in boards:
        for line in board:
            for num in line:
                # print(num[0] == number)
                if num[0] == number:
                    num[1] = 'y'
                # print(num)
        if checkBingo(board):
            currentBoard = board
            boom_pow = number
            boards = pydash.pull(boards, board)


print(currentBoard)

big_BING_BONG = 0
for line in currentBoard:
    for num in line:
        if num[1] == 'n':
            big_BING_BONG += num[0]

print(big_BING_BONG)
print(boom_pow)
print(boom_pow * big_BING_BONG)