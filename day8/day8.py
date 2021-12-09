import pydash as _

with open("day8/input.txt") as file:
    lines = file.read().splitlines()

lines = [line.split('|') for line in lines]
for i in range(len(lines)):
    lines[i] = [item.split() for item in lines[i]]

count = 0
for line in lines:
    for num in line[1]:
        if len(num) == 2 or len(num) == 3 or len(num) == 4 or len(num) == 7:
            count += 1


print("Day 8 Part 1:")
print(count)

print("Day 8 Part 2:")

currLine = lines[0]
# print(currLine)
class Display_7_Seg():
    seg0 = 0
    seg1 = 0 
    seg2 = 0
    seg3 = 0 
    seg4 = 0 
    seg5 = 0 
    seg6 = 0 
    def setSeg(self, s):
        if s == 0: self.seg0 = 1
        elif s == 1: self.seg1 = 1
        elif s == 2: self.seg2 = 1
        elif s == 3: self.seg3 = 1
        elif s == 4: self.seg4 = 1
        elif s == 5: self.seg5 = 1
        elif s == 6: self.seg6 = 1
    
    def calcNum(self):
        if (self.seg0 and self.seg1 and self.seg2 and not self.seg3 and self.seg4 and self.seg5 and self.seg6):
            return 0
        elif (not self.seg0 and not self.seg1 and self.seg2 and not self.seg3 and not self.seg4 and self.seg5 and not self.seg6):
            return 1
        elif (self.seg0 and not self.seg1 and self.seg2 and self.seg3 and self.seg4 and not self.seg5 and self.seg6):
            return 2
        elif (self.seg0 and not self.seg1 and self.seg2 and self.seg3 and not self.seg4 and self.seg5 and self.seg6):
            return 3
        elif (not self.seg0 and self.seg1 and self.seg2 and self.seg3 and not self.seg4 and self.seg5 and not self.seg6):
            return 4
        elif (self.seg0 and self.seg1 and not self.seg2 and self.seg3 and not self.seg4 and self.seg5 and self.seg6):
            return 5
        elif (self.seg0 and self.seg1 and not self.seg2 and self.seg3 and self.seg4 and self.seg5 and self.seg6):
            return 6
        elif (self.seg0 and not self.seg1 and self.seg2 and not self.seg3 and not self.seg4 and self.seg5 and not self.seg6):
            return 7
        elif (self.seg0 and self.seg1 and self.seg2 and self.seg3 and self.seg4 and self.seg5 and self.seg6):
            return 8
        elif (self.seg0 and self.seg1 and self.seg2 and self.seg3 and not self.seg4 and self.seg5 and self.seg6):
            return 9

totalVal = 0
for line in lines:
    print(line)
    possibilities = [['a','b','c','d','e','f','g'],['a','b','c','d','e','f','g'],['a','b','c','d','e','f','g'],['a','b','c','d','e','f','g'],['a','b','c','d','e','f','g'],['a','b','c','d','e','f','g'],['a','b','c','d','e','f','g']]
    fives = []
    sixes = []
    # print(possibilities)
    for signal in line[0]:
        if len(signal) == 2:
            # pull the two chars from non-valid segments
            _.pull(possibilities[0], signal[0], signal[1])
            _.pull(possibilities[1], signal[0], signal[1])
            _.pull(possibilities[3], signal[0], signal[1])
            _.pull(possibilities[4], signal[0], signal[1])
            _.pull(possibilities[6], signal[0], signal[1])

            # pull all other chars from segments where these two chars must go
            otherChars = _.pull(['a','b','c','d','e','f','g'], signal[0], signal[1])
            for c in otherChars:
                possibilities[2] = _.pull(possibilities[2], c)
                possibilities[5] = _.pull(possibilities[5], c)

        elif len(signal) == 3:
            # pull the three chars from non-valid segments
            possibilities[1] = _.pull(possibilities[1], signal[0], signal[1], signal[2])
            possibilities[3] = _.pull(possibilities[3], signal[0], signal[1], signal[2])
            possibilities[4] = _.pull(possibilities[4], signal[0], signal[1], signal[2])
            possibilities[6] = _.pull(possibilities[6], signal[0], signal[1], signal[2])

            # pull all other chars from segments where these three chars must go
            otherChars = _.pull(['a','b','c','d','e','f','g'], signal[0], signal[1], signal[2])
            for c in otherChars:
                possibilities[0] = _.pull(possibilities[0], c)
                possibilities[2] = _.pull(possibilities[2], c)
                possibilities[5] = _.pull(possibilities[5], c)

        elif len(signal) == 4:
            # pull the four chars from non-valid segments
            possibilities[0] = _.pull(possibilities[0], signal[0], signal[1], signal[2], signal[3])
            possibilities[4] = _.pull(possibilities[4], signal[0], signal[1], signal[2], signal[3])
            possibilities[6] = _.pull(possibilities[6], signal[0], signal[1], signal[2], signal[3])

            # pull all other chars from segments where these four chars must go
            otherChars = _.pull(['a','b','c','d','e','f','g'], signal[0], signal[1], signal[2], signal[3])
            for c in otherChars:
                possibilities[1] = _.pull(possibilities[1], c)
                possibilities[2] = _.pull(possibilities[2], c)
                possibilities[3] = _.pull(possibilities[3], c)
                possibilities[5] = _.pull(possibilities[5], c)

        elif len(signal) == 5:
            fives.append(signal)
        elif len(signal) == 6:
            sixes.append(signal)

    fivesCount = [0,0,0,0,0,0,0]
    print(fives)
    for f in fives:
        fivesCount[0] += f.count('a')
        fivesCount[1] += f.count('b')
        fivesCount[2] += f.count('c')
        fivesCount[3] += f.count('d')
        fivesCount[4] += f.count('e')
        fivesCount[5] += f.count('f')
        fivesCount[6] += f.count('g')

    print(fivesCount)
    letters = ['a','b','c','d','e','f','g']
    onesString = ""
    for i in range(len(fivesCount)):
        if fivesCount[i] == 1:
            onesString += letters[i]
    print("ones string")
    print(onesString)
    for i in range(len(fivesCount)):
        if fivesCount[i] == 1:
            # pull the two chars from non-valid segments
            _.pull(possibilities[0], onesString[0], onesString[1])
            _.pull(possibilities[2], onesString[0], onesString[1])
            _.pull(possibilities[3], onesString[0], onesString[1])
            _.pull(possibilities[5], onesString[0], onesString[1])
            _.pull(possibilities[6], onesString[0], onesString[1])

            # pull all other chars from segments where these two chars must go
            otherChars = _.pull(['a','b','c','d','e','f','g'], onesString[0], onesString[1])
            for c in otherChars:
                _.pull(possibilities[1], c)
                _.pull(possibilities[4], c)

        # elif fivesCount[i] == 2:
        # elif fivesCount[i] == 3:

    sixesCount = [0,0,0,0,0,0,0]
    for s in sixes:
        sixesCount[0] += s.count('a')
        sixesCount[1] += s.count('b')
        sixesCount[2] += s.count('c')
        sixesCount[3] += s.count('d')
        sixesCount[4] += s.count('e')
        sixesCount[5] += s.count('f')
        sixesCount[6] += s.count('g')

    twosString = ""
    for i in range(len(sixesCount)):
        if sixesCount[i] == 2:
            twosString += letters[i]
    print("twos string")
    print(twosString)
    for i in range(len(sixesCount)):
        if sixesCount[i] == 2:
            # pull the three chars from non-valid segments
            _.pull(possibilities[0], twosString[0], twosString[1], twosString[2])
            _.pull(possibilities[1], twosString[0], twosString[1], twosString[2])
            _.pull(possibilities[5], twosString[0], twosString[1], twosString[2])
            _.pull(possibilities[6], twosString[0], twosString[1], twosString[2])

            # pull all other chars from segments where these three chars must go
            otherChars = _.pull(['a','b','c','d','e','f','g'], twosString[0], twosString[1], twosString[2])
            print(otherChars)
            for c in otherChars:
                _.pull(possibilities[2], c)
                _.pull(possibilities[3], c)
                _.pull(possibilities[4], c)

    key = _.flatten(possibilities)
    print(key)


    val = ""
    for num in line[1]:
        display = Display_7_Seg()
        for c in num:
            segment = _.index_of(key, c)
            display.setSeg(segment)

        print(display.calcNum())
        val += str(display.calcNum())
            # print(c)
            # print(key)
            # val += possibilities[c]
        # print(output)
    val = int(val)
    print(val)
    totalVal += val

print("TOTAL:")
print(totalVal)