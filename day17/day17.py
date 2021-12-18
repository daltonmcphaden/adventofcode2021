with open("day17/input.txt") as file:
    targetArea = file.read()

class Coord():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    x = 0    
    y = 0

print(targetArea)
nums = targetArea.split('x=')[1]
x = nums.split(', y=')[0]
y = nums.split(', y=')[1]
x1 = int(x.split('..')[0])
x2 = int(x.split('..')[1])
y1 = int(y.split('..')[0])
y2 = int(y.split('..')[1])
x = range(x1,x2)
y = range(y1,y2)
print(x)
print(y)

pos = Coord(0,0)
velo = Coord(7,2)
yMaxSupreme = 0
count = 0
for i in range(70):
    print(i)
    for j in range(-250, 400):
        # if j % 100 == 0:
        #     print(j)
        pos = Coord(0,0)
        velo = Coord(i+1,j+1)

        step = 0
        maxSteps = 1500
        yMax = 0

        while (pos.x not in x or pos.y not in y) and step < maxSteps:
            pos.x += velo.x
            pos.y += velo.y
            yMax = max(yMax, pos.y)
            if velo.x > 0:
                velo.x -= 1
            elif velo.x < 0:
                velo.x += 1
            velo.y -= 1
            step += 1
        if step != maxSteps:
            count += 1
            # print("In zone on step", step)
            # print("initialVelo was", i+1, j+1)
            # if yMax > yMaxSupreme:
            #     yMaxSupreme = yMax
            #     print(yMaxSupreme)
            #     print(j)
            # print("Top Y coord was", yMax)
            # print((pos.x, pos.y))
        # else:
            # print("max step reached for initialVelo", i+1, j+1)

# print("yMaxSupreme", yMaxSupreme)
print("count", count)
