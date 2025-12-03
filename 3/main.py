with open("testinput.txt", "r") as inputFile:
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
        maxJoltage += str(max(lineList[:(-12+i)]))
        lineList = lineList[lineList.index(max(lineList[:(-13+i)]))+1:]
    print(maxJoltage)

print(totalJoltage)
