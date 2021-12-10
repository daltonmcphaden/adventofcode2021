import pydash as _

with open("day10/input.txt") as file:
    lines = file.read().splitlines()

lines = [list(line) for line in lines]

culprits = []
goodLines = []
for line in lines:
    stack = []
    valid = True
    for c in line:
        if c == '(' or c == '[' or c == '{' or c =='<':
            stack.append(c)

        elif c == ')':
            k = stack.pop()
            if k != '(':
                culprits.append(c)
                valid = False

        elif c == ']':
            k = stack.pop()
            if k != '[':
                culprits.append(c) 
                valid = False

        elif c == '}':
            k = stack.pop()
            if k != '{':
                culprits.append(c) 
                valid = False

        elif c == '>':
            k = stack.pop()
            if k != '<':
                culprits.append(c) 
                valid = False
    if valid:
        goodLines.append(line)

# print(len(goodLines))
# print(culprits)
res = 0
for c in culprits:
    if c == ')':
        res += 3
    elif c == ']':
        res += 57
    elif c == '}':
        res += 1197
    elif c == '>':
        res += 25137

print("Part 1 solution:")
print(res)

stack2s = []
for line in goodLines:
    stack1 = []
    stack2 = []

    for c in line:
        if c == '(':
            stack1.append(c)
            stack2.append(')')
        elif c == '[':
            stack1.append(c)
            stack2.append(']')
        elif c == '{':
            stack1.append(c)
            stack2.append('}')
        elif c =='<':
            stack1.append(c)
            stack2.append('>')
        else:
            stack1.pop()
            stack2.pop()
    stack2s.append(stack2)

scores = []
for s2 in stack2s:
    score = 0
    for s in reversed(s2):
        score *= 5
        if s == ')':
            score += 1
        elif s == ']':
            score += 2
        elif s == '}':
            score += 3
        elif s == '>':
            score += 4
    scores.append(score)
import statistics
print(statistics.median(scores))