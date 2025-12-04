with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
validRolls = 0

for rowIndex in range(len(inputRaw)):
    for columnIndex in range(len(inputRaw[0])):
        if inputRaw[rowIndex][columnIndex] == "@":
            neighbors = 0
            for dr, dc in directions:
                    checkingRow = rowIndex + dr
                    checkingColumn = columnIndex + dc
                    if 0 <= checkingRow < len(inputRaw) and 0 <= checkingColumn < len(inputRaw[0]):
                        if inputRaw[checkingRow][checkingColumn] == "@":
                            neighbors += 1
            if neighbors < 4:
                validRolls += 1

print(validRolls)

removedCount = 0
completed = False
inputRaw = [list(line.strip()) for line in inputRaw]

while not completed:
    removeQueue = []
    for rowIndex in range(len(inputRaw)):
        for columnIndex in range(len(inputRaw[0])):
            if inputRaw[rowIndex][columnIndex] == "@":
                neighbors = 0
                for dr, dc in directions:
                        checkingRow = rowIndex + dr
                        checkingColumn = columnIndex + dc
                        if 0 <= checkingRow < len(inputRaw) and 0 <= checkingColumn < len(inputRaw[0]):
                            if inputRaw[checkingRow][checkingColumn] == "@":
                                neighbors += 1
                if neighbors < 4:
                    removeQueue.append([rowIndex, columnIndex])

    if removeQueue:
        for row, column in removeQueue:
            inputRaw[row][column] = "."
            removedCount += 1
    else:
        completed = True

print(removedCount)


