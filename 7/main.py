with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = list(inputRaw[lineIndex].strip())
        
splitCounter = 0
iterationCounter = 0
visited = set()
visited_splitters = set()


def simulateTachyonBeam(startRow, startColumn, manifold):
    global splitCounter
    global iterationCounter
    
    iterationCounter += 1
    print(iterationCounter)
        
    currentRow = startRow + 1

    if (startRow, startColumn) in visited:
        return
    visited.add((startRow, startColumn))

    while True:
        if not (0 <= currentRow < len(manifold) and 0 <= startColumn < len(manifold[0])):
            return
        if manifold[currentRow][startColumn] == ".":
            if currentRow == len(manifold) - 1:
                return
            currentRow += 1
            continue
        elif manifold[currentRow][startColumn] == "^":
            if (currentRow, startColumn) in visited_splitters:
                return
            visited_splitters.add((currentRow, startColumn))
            splitCounter += 1
            if startColumn - 1 >= 0:
                simulateTachyonBeam(currentRow, startColumn - 1, manifold)
            if startColumn + 1 < len(manifold[0]):
                simulateTachyonBeam(currentRow, startColumn + 1, manifold)
            return

simulateTachyonBeam(0, inputRaw[0].index("S"), inputRaw)

print(splitCounter)


        