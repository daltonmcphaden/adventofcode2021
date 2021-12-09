import pydash as _

with open("day9/input.txt") as file:
    lines = file.read().splitlines()

lines = [list(line) for line in lines]
for i in range(len(lines)):
    lines[i] = [int(s) for s in lines[i]]

def checkNeighbors(j, k, basin):
    val = lines[j][k]
    up = lines[j-1][k] if (j-1) >= 0 else 10
    down = lines[j+1][k] if (j+1) < vSize else 10
    left = lines[j][k-1] if (k-1) >= 0 else 10
    right = lines[j][k+1] if (k+1) < hSize else 10
    if up > val and up < 9:
        basin.append((j-1, k))
        checkNeighbors(j-1, k, basin)
    if down > val and down < 9:
        basin.append((j+1, k))
        checkNeighbors(j+1, k, basin)
    if left > val and left < 9:
        basin.append((j, k-1))
        checkNeighbors(j, k-1, basin)
    if right > val and right < 9:
        basin.append((j, k+1))
        checkNeighbors(j, k+1, basin)

basins = []
lowPoints = []
for j in range(len(lines)):
    hSize = len(lines[j])
    vSize = len(lines)
    for k in range(len(lines[j])):
        val = lines[j][k]
        up = lines[j-1][k] if (j-1) >= 0 else 10
        down = lines[j+1][k] if (j+1) < vSize else 10
        left = lines[j][k-1] if (k-1) >= 0 else 10
        right = lines[j][k+1] if (k+1) < hSize else 10

        if val < up and val < down and val < left and val < right:
            lowPoints.append(val)
            basin = []
            basin.append((j,k))
            checkNeighbors(j, k, basin)
            basins.append(basin)

for b in range(len(basins)):
    basins[b] = _.uniq(basins[b])
    basins[b] = len(basins[b])

basins.sort(reverse=True)
print(basins)
top3 = basins[:3]
result = 1
for thing in top3:
    result *= thing

print(result)
# print(lowPoints)
sum = 0
for point in lowPoints:
    sum += point + 1
# print(sum)

