with open("day3/input.txt") as file:
    input = file.read().splitlines()

print("Day 2 Part 1:")
counts = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
for number in input:
    for digit in range(len(number)):
        if (number[digit] == '0'):
            counts[digit][0] += 1
        else:
            counts[digit][1] += 1

gamma_rate = []
epsilon_rate = []
for i in range(len(counts)):
    if counts[i][0] > counts[i][1]:
        gamma_rate.append(0)
        epsilon_rate.append(1)
    else:
        gamma_rate.append(1)
        epsilon_rate.append(0)

print(gamma_rate)
print(epsilon_rate)

gamma_rate_decimal = 0
i = len(gamma_rate) - 1
for bit in gamma_rate:
    gamma_rate_decimal += bit * 2**i
    i -= 1

epsilon_rate_decimal = 0
i = len(epsilon_rate) - 1
for bit in epsilon_rate:
    epsilon_rate_decimal += bit * 2**i
    i -= 1

print(gamma_rate_decimal)
print(epsilon_rate_decimal)

print(gamma_rate_decimal * epsilon_rate_decimal)

print("Day 2 Part 2:")

import numpy as np

zeroesCount = 0
onesCount = 0
zeroesList = []
onesList = []

oxygenList = input

for i in range(len(input[0])):

    for number in oxygenList:
        if (number[i] == '0'):
            zeroesCount += 1
            zeroesList.append(number)
        else:
            onesCount += 1
            onesList.append(number)

    if zeroesCount > onesCount:
        oxygenList = np.intersect1d(oxygenList, zeroesList)
    else:
        oxygenList = np.intersect1d(oxygenList, onesList)
    
    zeroesCount = 0
    onesCount = 0
    zeroesList = []
    onesList = []

print(oxygenList)

zeroesCount = 0
onesCount = 0
zeroesList = []
onesList = []

co2List = input

for i in range(len(input[0])):
    if len(co2List) == 1:
        break

    for number in co2List:
        if (number[i] == '0'):
            zeroesCount += 1
            zeroesList.append(number)
        else:
            onesCount += 1
            onesList.append(number)

    if zeroesCount <= onesCount:
        co2List = np.intersect1d(co2List, zeroesList)
    else:
        co2List = np.intersect1d(co2List, onesList)
    
    zeroesCount = 0
    onesCount = 0
    zeroesList = []
    onesList = []

print(co2List)

oxygen_decimal = int(oxygenList[0], 2)

co2_decimal = int(co2List[0], 2)


print(oxygen_decimal * co2_decimal)