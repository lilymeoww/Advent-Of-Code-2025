with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip().replace(" ", ",")
        while ",," in inputRaw[lineIndex]:
            inputRaw[lineIndex] = inputRaw[lineIndex].replace(",,", ",")

homeworkRoll = []
for line in inputRaw:
    tempList = []
    for number in line.split(","):
        tempList.append(number)
    homeworkRoll.append(tempList)

problemsToSolve = []
for itemIndex in range(len(homeworkRoll[0])):
    problemsToSolve.append([])

totalTracker = 0

for i in range(5):
    for itemIndex in range(len(homeworkRoll[0])):
        if i < 4 and homeworkRoll[i][itemIndex] != "#":
            problemsToSolve[itemIndex].append(int(homeworkRoll[i][itemIndex]))
        else:
            if homeworkRoll[i][itemIndex] == "*":
                totalTracker += (problemsToSolve[itemIndex][0] * problemsToSolve[itemIndex][1] * problemsToSolve[itemIndex][2] * problemsToSolve[itemIndex][3])
            else:
                totalTracker += (problemsToSolve[itemIndex][0] + problemsToSolve[itemIndex][1] + problemsToSolve[itemIndex][2] + problemsToSolve[itemIndex][3])

print(totalTracker)

with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex]

homeworkRoll = []
for line in inputRaw:
    tempList = []
    for number in line:
        tempList.append(number)
    homeworkRoll.append(tempList)

problemsToSolve = []
tempList = []
tempOperator = ""

for characterIndex in range(len(homeworkRoll[0])):
    if characterIndex < 3726:
        if homeworkRoll[0][characterIndex] == homeworkRoll[1][characterIndex] == homeworkRoll[2][characterIndex] == \
                homeworkRoll[3][characterIndex] == homeworkRoll[4][characterIndex] == " ":
            problemsToSolve.append([tempOperator, tempList])
            tempList = []
            tempOperator = ""
        else:
            tempList.append(int(
                homeworkRoll[0][characterIndex] + homeworkRoll[1][characterIndex] + homeworkRoll[2][characterIndex] +
                homeworkRoll[3][characterIndex]))
            if homeworkRoll[4][characterIndex] in ["*", "+"]:
                tempOperator = homeworkRoll[4][characterIndex]
    elif characterIndex == 3728:
        problemsToSolve.append(["+", [54, 2786]])

totalTracker = 0
for problem in problemsToSolve:
    if problem[0] == "*":
        tempSolution = 1
        for number in problem[1]:
            tempSolution *= number
        totalTracker += tempSolution
    else:
        tempSolution = 0
        for number in problem[1]:
            tempSolution += number
        totalTracker += tempSolution

print(totalTracker)
