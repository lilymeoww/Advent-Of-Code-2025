import math

with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

idRanges = inputRaw[0].split(",")
totalValid = 0

for idRange in idRanges:
    lowId = int(idRange.split("-")[0])
    highId = int(idRange.split("-")[1]) + 1
    for i in range(highId - lowId):
        currentId = str(i + lowId)
        # print(currentId)
        if len(currentId) % 2 == 0:
            if currentId[:int(len(currentId) / 2)] == currentId[int(len(currentId) / 2):]:
                # print(currentId[:int(len(currentId) / 2)])
                # print(currentId[int(len(currentId) / 2):])
                totalValid += int(currentId)
        else:
            if currentId[:int((len(currentId)-1) / 2)] == currentId[int((len(currentId)-1) / 2):]:
                pass
                # totalValid += int(currentId)

print(totalValid)

totalValid = 0
validIds = []

for idRange in idRanges:
    lowId = int(idRange.split("-")[0])
    highId = int(idRange.split("-")[1]) + 1
    for i in range(highId - lowId):
        currentId = str(i + lowId)
        for j in range(len(currentId) // 2):
            if currentId[:j+1] * (len(currentId) // (j+1)) == currentId:
                if currentId not in validIds:
                    totalValid += int(currentId)
                    validIds.append(currentId)
                    # print(currentId)

print(totalValid)



