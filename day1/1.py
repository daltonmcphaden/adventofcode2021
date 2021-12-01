with open("day1/input.txt") as file:
    measurements = file.readlines()

print("Day 1 Part 1:")

count1 = 0
for i in range(1, len(measurements)):
    if int(measurements[i]) > int(measurements[i-1]):
        count1 += 1
    
print(count1)

print("Day 1 Part 2:")

count2 = 0
for i in range(3, len(measurements)):
    if (int(measurements[i]) > int(measurements[i-3])):
        count2 += 1
    
print(count2)