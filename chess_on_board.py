import fileinput

memoryCache = {}

# helper function to check if character is a digit
def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# returns dictionary of all digits to (row,col)
def getDigitPositions(numRows, numCols, grid):
    digitPositions = {}
    for row in range(numRows):
        for col in range(numCols):
            if isNumber(grid[row][col]):
                digitPositions[int(grid[row][col])] = (row, col)
    return digitPositions

# recursively counts the valid moves for a knight
def recurseCountKnight(movesLeft, row, col, numRows, numCols, grid, digitPositions, path, cache):
        
    if row < 0 or row >= numRows or col < 0 or col >= numCols:
        # out of bounds
        return 0
       
    if not isNumber(grid[row][col]):
        # is not a digit
        return 0
        
    path.append(grid[row][col])
    
    if not movesLeft:
        # no moves left
        cache.add(tuple(path))
        path.pop()
        return 1
    
    # count all valid moves in the L shape
    countValidMoves = 0
    countValidMoves += recurseCountKnight(movesLeft-1, row-2, col-1, numRows, numCols, grid, digitPositions, path, cache)
    countValidMoves += recurseCountKnight(movesLeft-1, row-2, col+1, numRows, numCols, grid, digitPositions, path, cache)
    countValidMoves += recurseCountKnight(movesLeft-1, row-1, col-2, numRows, numCols, grid, digitPositions, path, cache)
    countValidMoves += recurseCountKnight(movesLeft-1, row-1, col+2, numRows, numCols, grid, digitPositions, path, cache)
    countValidMoves += recurseCountKnight(movesLeft-1, row+2, col-1, numRows, numCols, grid, digitPositions, path, cache)
    countValidMoves += recurseCountKnight(movesLeft-1, row+2, col+1, numRows, numCols, grid, digitPositions, path, cache)
    countValidMoves += recurseCountKnight(movesLeft-1, row+1, col-2, numRows, numCols, grid, digitPositions, path, cache)
    countValidMoves += recurseCountKnight(movesLeft-1, row+1, col+2, numRows, numCols, grid, digitPositions, path, cache)
        
    path.pop()
    return countValidMoves

# count knight moves using memoization with cache of (current digit, number of moves left)
# to valid move count.     
def recurseCountKnightDP(movesLeft, row, col, numRows, numCols, grid, digitPositions, path, cache):
    if row < 0 or row >= numRows or col < 0 or col >= numCols:
        # out of bounds
        return 0
       
    if not isNumber(grid[row][col]):
        # is not a digit
        return 0
        
    path.append(grid[row][col])
    
    # memory cache key is a tuple of the current digit and the number of moves left
    cacheKey = (grid[row][col], movesLeft)
    if cacheKey in memoryCache:
        #print "in cache for", pathTuple
        return memoryCache[cacheKey]
    
    if not movesLeft:
        # no moves left
        cache.add(tuple(path))
        path.pop()
        return 1
    
    # count all valid moves in the L shape
    countValidMoves = 0
    countValidMoves += recurseCountKnightDP(movesLeft-1, row-2, col-1, numRows, numCols, grid, digitPositions, path, cache)
    countValidMoves += recurseCountKnightDP(movesLeft-1, row-2, col+1, numRows, numCols, grid, digitPositions, path, cache)
    countValidMoves += recurseCountKnightDP(movesLeft-1, row-1, col-2, numRows, numCols, grid, digitPositions, path, cache)
    countValidMoves += recurseCountKnightDP(movesLeft-1, row-1, col+2, numRows, numCols, grid, digitPositions, path, cache)
    countValidMoves += recurseCountKnightDP(movesLeft-1, row+2, col-1, numRows, numCols, grid, digitPositions, path, cache)
    countValidMoves += recurseCountKnightDP(movesLeft-1, row+2, col+1, numRows, numCols, grid, digitPositions, path, cache)
    countValidMoves += recurseCountKnightDP(movesLeft-1, row+1, col-2, numRows, numCols, grid, digitPositions, path, cache)
    countValidMoves += recurseCountKnightDP(movesLeft-1, row+1, col+2, numRows, numCols, grid, digitPositions, path, cache)
    
    memoryCache[cacheKey] = countValidMoves
    path.pop() 
    return countValidMoves
    
# recursively counts the valid moves for a bishop        
def recurseCountBishop(movesLeft, row, col, numRows, numCols, grid, digitPositions, path, cache):
    if row < 0 or row >= numRows or col < 0 or col >= numCols:
        # out of bounds
        return 0
       
    if not isNumber(grid[row][col]):
        # is not a digit
        return 0
        
    path.append(grid[row][col])
    
    if not movesLeft:
        # no moves left
        cache.add(tuple(path))
        path.pop()
        return 1
    
    # get all valid moves in 4 diagonal directions
    rowIdx = row
    colIdx = col
    countValidMoves = 0
    while(rowIdx < numRows and colIdx < numCols):
        rowIdx += 1
        colIdx += 1
        countValidMoves += recurseCountBishop(movesLeft-1, rowIdx, colIdx, numRows, numCols, grid, digitPositions, path, cache)
    
    rowIdx = row
    colIdx = col
    while(rowIdx < numRows and colIdx >= 0):
        rowIdx += 1
        colIdx -= 1
        countValidMoves += recurseCountBishop(movesLeft-1, rowIdx, colIdx, numRows, numCols, grid, digitPositions, path, cache)    
        
    rowIdx = row
    colIdx = col
    while(rowIdx >= 0 and colIdx < numCols):
        rowIdx -= 1
        colIdx += 1
        countValidMoves += recurseCountBishop(movesLeft-1, rowIdx, colIdx, numRows, numCols, grid, digitPositions, path, cache)
        
    rowIdx = row
    colIdx = col
    while(rowIdx >= 0 and colIdx >= 0):
        rowIdx -= 1
        colIdx -= 1
        countValidMoves += recurseCountBishop(movesLeft-1, rowIdx, colIdx, numRows, numCols, grid, digitPositions, path, cache)
        
    path.pop()
    return countValidMoves

# count bishop moves using memoization with cache of (current digit, number of moves left)
# to valid move count.    
def recurseCountBishopDP(movesLeft, row, col, numRows, numCols, grid, digitPositions, path, cache):   
    if row < 0 or row >= numRows or col < 0 or col >= numCols:
        # out of bounds
        return 0
       
    if not isNumber(grid[row][col]):
        # is not a digit
        return 0
        
    path.append(grid[row][col])
    
    # cache key is a tuple of the current digit and number of moves left 
    cacheKey = (grid[row][col], movesLeft)
    if cacheKey in memoryCache:
        #print "in cache for", pathTuple
        return memoryCache[cacheKey]
    
    if not movesLeft:
        # no moves left
        cache.add(tuple(path))
        path.pop()
        return 1
    
    # get all valid moves in 4 diagonal directions
    rowIdx = row
    colIdx = col
    countValidMoves = 0
    while(rowIdx < numRows and colIdx < numCols):
        rowIdx += 1
        colIdx += 1
        countValidMoves += recurseCountBishopDP(movesLeft-1, rowIdx, colIdx, numRows, numCols, grid, digitPositions, path, cache)
    
    rowIdx = row
    colIdx = col
    while(rowIdx < numRows and colIdx >= 0):
        rowIdx += 1
        colIdx -= 1
        countValidMoves += recurseCountBishopDP(movesLeft-1, rowIdx, colIdx, numRows, numCols, grid, digitPositions, path, cache)    
        
    rowIdx = row
    colIdx = col
    while(rowIdx >= 0 and colIdx < numCols):
        rowIdx -= 1
        colIdx += 1
        countValidMoves += recurseCountBishopDP(movesLeft-1, rowIdx, colIdx, numRows, numCols, grid, digitPositions, path, cache)
        
    rowIdx = row
    colIdx = col
    while(rowIdx >= 0 and colIdx >= 0):
        rowIdx -= 1
        colIdx -= 1
        countValidMoves += recurseCountBishopDP(movesLeft-1, rowIdx, colIdx, numRows, numCols, grid, digitPositions, path, cache)
    
    memoryCache[cacheKey] = countValidMoves    
    path.pop()
    return countValidMoves

# counts all sequences of moves at the possible starting points
def countAllSequences(piece, numberLength, validStartingDigits, numRows, numCols, grid):
    if numberLength < 1:
        return 0
        
    digitPositions = getDigitPositions(numRows, numCols, grid)
    
    # cache contains all the paths (not needed for this problem but helpful)
    cache = set()
    count = 0
    for startingDigit in validStartingDigits:
        if startingDigit not in digitPositions:
            continue
            
        startingRow, startingCol = digitPositions[int(startingDigit)]
        path = []
        if piece == 'knight':
            #count += recurseCountKnight(numberLength-1, startingRow, startingCol, numRows, numCols, grid, digitPositions, path, cache)
            count += recurseCountKnightDP(numberLength-1, startingRow, startingCol, numRows, numCols, grid, digitPositions, path, cache)
        else:
            #count += recurseCountBishop(numberLength-1, startingRow, startingCol, numRows, numCols, grid, digitPositions, path, cache)
            count += recurseCountBishopDP(numberLength-1, startingRow, startingCol, numRows, numCols, grid, digitPositions, path, cache)          

    #print sorted(list(cache))
    return count    
        
# processes the inputs and extracts the neccessary inputs
def processInput():
    lines = []
    for line in fileinput.input():
        lines.append(line.strip())
        
    piece = lines[0]
    numberLength = int(lines[1])
    validStartingDigits = [int(digit) for digit in lines[2].split() if digit]
    numRows = int(lines[3])
    numCols = int(lines[4])
    grid = []
    
    for row in range(numRows):
        grid.append(lines[row+5].split())
        
    return piece, numberLength, validStartingDigits, numRows, numCols, grid
        
def main():
    piece, numberLength, validStartingDigits, numRows, numCols, grid = processInput()
    #print piece
    #print numberLength
    #print validStartingDigits
    #print numRows
    #print numCols
    #print grid
    count = countAllSequences(piece, numberLength, validStartingDigits, numRows, numCols, grid)
    print count

# main for testing only
def main2():
    grid = [['1','2','3'], ['4','5','6'], ['7','8','9'], ['*','0','#']]
    #count = countAllSequences('knight', 2, [2,3,4,5,6,7,8,9], 4, 3, grid)
    count = countAllSequences('bishop', 9, [2,3,4,5,6,7,8,9], 4, 3, grid)
    print count
    
main()
#main2()