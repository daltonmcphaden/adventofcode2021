with open("day2/input.txt") as file:
    directions = file.readlines()

print("Day 2 Part 1:")

horizontal = 0
depth = 0

for d in directions:
    type = d.split()[0]
    magnitude = int(d.split()[1])
    if type == 'forward':
        horizontal += magnitude
    elif type == 'up':
        depth -= magnitude
    elif type == 'down':
        depth += magnitude

print(horizontal)
print(depth)
print(horizontal*depth)

print("Day 2 Part 2:")

horizontal = 0
depth = 0
aim = 0

for d in directions:
    type = d.split()[0]
    magnitude = int(d.split()[1])
    if type == 'forward':
        horizontal += magnitude
        depth += aim * magnitude
    elif type == 'up':
        aim -= magnitude
    elif type == 'down':
        aim += magnitude
        
print(horizontal)
print(depth)
print(horizontal*depth)