with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

meow = 0
currentPos = 50

for instruction in inputRaw:
    if instruction[0] == "L":
        currentPos -= int(instruction[1:])
        while currentPos < 0 or currentPos > 99:
            currentPos %= 100
    elif instruction[0] == "R":
        currentPos += int(instruction[1:])
        while currentPos < 0 or currentPos > 99:
            currentPos %= 100

    if currentPos == 0:
        meow += 1

print(meow)
meow2 = 0
currentPos = 50

for instruction in inputRaw:
    if instruction[0] == "L":
        step = int(instruction[1:])
        for i in range(step):
            currentPos -= 1
            while currentPos < 0 or currentPos > 99:
                currentPos %= 100
            if currentPos == 0:
                meow2 += 1
        while currentPos < 0 or currentPos > 99:
            currentPos %= 100
        print(currentPos)
    elif instruction[0] == "R":
        step = int(instruction[1:])
        for i in range(step):
            currentPos += 1
            while currentPos < 0 or currentPos > 99:
                currentPos %= 100
            if currentPos == 0:
                meow2 += 1
        while currentPos < 0 or currentPos > 99:
            currentPos %= 100

print(meow2)