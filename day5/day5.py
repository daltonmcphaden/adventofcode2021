import pydash as _
import numpy as np
import matplotlib.pyplot as plt

with open("day5/input.txt") as file:
    lines = file.read().splitlines()
    
for i in range(len(lines)):
    lines[i] = lines[i].split(' -> ')
    for j in range(len(lines[i])):
        lines[i][j] = lines[i][j].split(',')
    lines[i] = _.flatten(lines[i])
    lines[i] = [int(k) for k in lines[i]]

# x1,y1 -> x2,y2
print(len(lines))

oceanFloor = np.zeros((1000,1000))

def drawLine(coords, map):
    x1 = coords[0]
    y1 = coords[1]
    x2 = coords[2]
    y2 = coords[3]
    # x is the column, y is the row.
    if (x1 == x2):
        # same x
        col = x1
        if (y1 > y2):
            temp = y1
            y1 = y2
            y2 = temp
        for row in range(y1, y2 + 1):
            map[row][col] += 1

    elif (y1 == y2):
        # same y
        row = y1
        if (x1 > x2):
            temp = x1
            x1 = x2
            x2 = temp
        for col in range(x1, x2 + 1):
            map[row][col] += 1
            
    else:
        print(coords)
        length = abs(x1 - x2)
        if (x1 < x2 and y1 < y2):
            for i in range(length + 1):
                map[i + y1][i + x1] += 1
        elif (x1 > x2 and y1 < y2):
            for i in range(length + 1):
                map[i + y1][x1 - i] += 1
        elif (x1 < x2 and y1 > y2):
            for i in range(length + 1):
                map[y1 - i][i + x1] += 1
        elif (x1 > x2 and y1 > y2):
            for i in range(length + 1):
                map[y1 - i][x1 - i] += 1
        

for line in lines:
    drawLine(line, oceanFloor)

# p = [
#     [0,0,0,0],
#     [0,0,0,0],
#     [0,0,0,0],
#     [0,0,0,0]
# ]

# [
#     [0, 0, 0, 0], 
#     [1, 1, 1, 0], 
#     [0, 0, 0, 0], 
#     [0, 0, 0, 0]]

# drawLine([0,1,2,1], p)
# drawLine([1,1,3,1], p)
# print(p)

# print(oceanFloor[45])
plt.imshow(oceanFloor)
plt.show()
count = 0
for row in range(len(oceanFloor)):
    for col in range(len(oceanFloor[row])):
        if (oceanFloor[row][col] > 1):
            count += 1
print(count)