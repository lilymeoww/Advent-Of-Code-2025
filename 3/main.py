with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

totalJoltage = 0
for line in inputRaw:
    lineList = [int(char) for char in line]
    maxJoltage = int(str(max(lineList[:-1])) + str(max(lineList[lineList.index(max(lineList[:-1])) + 1:])))
    # print(maxJoltage)
    totalJoltage += maxJoltage

print(totalJoltage)
