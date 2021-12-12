with open("day11/input.txt") as file:
    lines = file.read().splitlines()

for i in range(len(lines)):
    lines[i] = [int(s) for s in lines[i]]

def increaseNeighbors(j, k):
    
    try: lines[j+1][k] += 1 
    except IndexError: pass
    try: lines[j+1][k+1] += 1
    except IndexError: pass
    if k-1 >= 0:
        try: lines[j+1][k-1] += 1
        except IndexError: pass
    try: lines[j][k+1] += 1
    except IndexError: pass
    if k-1 >= 0 and j-1 >= 0:
        try: lines[j-1][k-1] += 1
        except IndexError: pass
    if j-1 >= 0:
        try: lines[j-1][k+1] += 1
        except IndexError: pass
    if j-1 >= 0:
        try: lines[j-1][k] += 1
        except IndexError: pass
    if k-1 >= 0:
        try: lines[j][k-1] += 1
        except IndexError: pass

# do something 100 times (400 times to see when they all flash together)
flashCount = 0
for i in range(400):
    
    flashed = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
    moreFlashes = True

    # increase all energy levels by 1
    for j in range(len(lines)):
        for k in range(len(lines[j])):
            lines[j][k] += 1
    
    # flash phase
    while (moreFlashes):
        for j in range(len(lines)):
            for k in range(len(lines[j])):
                if lines[j][k] > 9 and flashed[j][k] == 0:
                    # if j == 
                    flashed[j][k] = 1
                    flashCount += 1
                    increaseNeighbors(j, k)

        # check if there are more flashes to happen this round
        moreFlashes = False
        for j in range(len(lines)):
            for k in range(len(lines[j])):
                if lines[j][k] > 9 and flashed[j][k] == 0:
                    moreFlashes = True
                
    # set those that flashed to zero at end of round
    count = 0
    for a in range(len(flashed)):
        for b in range(len(flashed[a])):
            if flashed[a][b] == 1:
                count += 1
                lines[a][b] = 0
    
    if count == 100:
        print("All flashes:", i + 1)
    # print(lines)
    # print("flashed:")
    # print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
    #   for row in flashed]))
    # print("lines after this round:")
    # print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
    #   for row in lines]))
    # print("Flashes this round :", flashCount)

print(flashCount)