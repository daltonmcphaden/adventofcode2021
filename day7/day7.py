import pydash as _

with open("day7/input.txt") as file:
    crabs = file.read().split(',')

for i in range(len(crabs)):
    crabs[i] = int(crabs[i])

maxDistance = _.max_(crabs)

costs = [0] * maxDistance

def Calc(a, b):
    distance = abs(a-b)
    sum = 0
    while distance > 0:
        sum += distance
        distance -= 1

    return sum

for i in range(len(costs)):
    print(i)
    for crab in crabs:
        costs[i] += Calc(crab, i)
        # costs[i] += abs(crab - i)
        # make more efficient here by keeping min

print(_.min_(costs))