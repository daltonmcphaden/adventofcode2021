with open("day14/input.txt") as file:
    lines = file.read().split("\n\n")

polymer = lines[0]
rules = [s for s in lines[1].split("\n")]
rules = dict(x.split(" -> ") for x in rules)

def incrementDict(dict, key, v = 1):
    if key in dict:
        dict[key] += v
    else:
        dict[key] = v

pairs = {}
chars = {}
for i in range(len(polymer)-1):
    incrementDict(chars, polymer[i])
    incrementDict(pairs, polymer[i:i+2])

# count the last char in the list
incrementDict(chars, polymer[-1])

for i in range(40):
    newPairs = {}
    for pair, v in pairs.items():
        if v > 0:
            newC = rules[pair]  # get new char
            p1 = pair[0] + newC         # new pair 1
            p2 = newC + pair[1]         # new pair 2
            incrementDict(chars, newC, v)  #increment that char v number of times
            incrementDict(newPairs, p1, v)
            incrementDict(newPairs, p2, v)
    
    pairs = newPairs

vals = [i for i in chars.values() if i != 0]
print(vals)
print(max(vals) - min(vals))
