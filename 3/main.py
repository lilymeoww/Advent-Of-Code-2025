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

totalJoltage = 0
for line in inputRaw:
    maxJoltage = ""
    lineList = [int(char) for char in line]
    for i in range(12):
        if i != 11:
            maxJoltage += str(max(lineList[:-11+i]))
            # print(f"chose max {maxJoltage[-1]} from {lineList[:(-11+i)]}, now {maxJoltage}")
            lineList = lineList[lineList.index(max(lineList[:-11+i])) + 1:]
            # print(f"New list: {lineList}")
        else:
            maxJoltage += str(max(lineList))
            # print(f"chose max {maxJoltage[-1]} from {lineList}, now {maxJoltage}")

    totalJoltage += int(maxJoltage)
    # print(maxJoltage)

print(totalJoltage)
