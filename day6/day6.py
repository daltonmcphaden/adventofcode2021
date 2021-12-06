

with open("day6/input.txt") as file:
    initialFish = file.read().split(',')

for i in range(len(initialFish)):
    initialFish[i] = int(initialFish[i])

states = [0]*10
print(states)

for num in initialFish:
    states[num] += 1

print(states)

for i in range(256):

    for k in range(len(states)):
        if k == 0:
            states[9] += states[k]
            states[7] += states[k]
            states[k] = 0
        else:
            states[k-1] += states[k]
            states[k] -= states[k]

print(sum(states))