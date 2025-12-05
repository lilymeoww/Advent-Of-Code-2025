with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

validRanges = []
for validRange in inputRaw[:177]:
    firstValid = int(validRange.split("-")[0])
    lastValid = int(validRange.split("-")[1])
    validRanges.append([firstValid, lastValid])

count = 0
for ingredientId in inputRaw[178:]:
    for firstValid, lastValid in validRanges:
        if firstValid <= int(ingredientId) <= lastValid:
            count += 1
            break

print(count)

validRanges.sort()
startRange, endRange = validRanges[0]
validRangesNew = []

for startRange2, endRange2 in validRanges[1:]:
    if startRange2 <= endRange:
        endRange = endRange if endRange > endRange2 else endRange2
    else:
        validRangesNew.append([startRange, endRange])
        startRange = startRange2
        endRange = endRange2

validRangesNew.append([startRange, endRange])
count = 0
for firstValid, lastValid in validRangesNew:
    count += lastValid - firstValid + 1
print(count)