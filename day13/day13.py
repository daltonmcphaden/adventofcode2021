with open("day13/input.txt") as file:
    dots = file.read().split("\n\n")
folds = dots[1].splitlines()
dots = dots[0].splitlines()
dots = [s.split(',') for s in dots]

def special_print(m):
    print('\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in m]))

def foldLocation(a, b):
    if a == '#' or b == '#':
        return '#'
    else:
        return '.'

maxX = 0
maxY = 0
for dot in dots:
    if int(dot[0]) > maxX:
        maxX = int(dot[0])
    if int(dot[1]) > maxY:
        maxY = int(dot[1])

print(maxX)
print(maxY)

matrix = []
for i in range(maxY+1):
    row = []
    for j in range(maxX+1):
        row.append('.')
    matrix.append(row)

for dot in dots:
    x = int(dot[0])
    y = int(dot[1])
    matrix[y][x] = '#'


for fold in folds:
    direction = fold.split()[2].split("=")[0]
    val = int(fold.split()[2].split("=")[1])
    print(direction)
    print(val)
    if direction == 'y':
        m1 = matrix[0:val]
        m2 = matrix[val+1:]
        # special_print(m1)
        # special_print(m2)
        for j in range(len(m1)):
            # print(m2[-1 - j])
            for i in range(len(m1[j])):
                m1[j][i] = foldLocation(m1[j][i], m2[-1-j][i])

        matrix = m1
    
    elif direction == 'x':
        m1 = []
        m2 = []
        for row in matrix:
            m1.append(row[0:val])
            m2.append(row[val+1:])

        for j in range(len(m1)):
            for i in range(len(m1[j])):
                m1[j][i] = foldLocation(m1[j][i], m2[j][-1-i])

        matrix = m1

special_print(m1)

    