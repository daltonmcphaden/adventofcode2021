with open("day3/input.txt") as file:
    input = file.read().splitlines()

print("Day 2 Part 1:")
size = len(input[0])
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