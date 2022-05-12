N = int(input("Enter the value of N"))
board = []


# Making board of N size
# Defining the board that we are going to work on
def getBoard():
    for i in range(N):
        nthList = []
        for j in range(N):
            nthList.append(0)
        board.append(nthList)


def printBoard():
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print(" ")


# Check if particular queen is safe at row,col or not
def isSafe(row, col):
    for i in range(N):
        if board[row][i] == 1:
            return False

    for j in range(N):
        if board[j][col] == 1:
            return False

    #     Check in Diagonal Diections
    i = row - 1
    j = col - 1
    # Left Diagonal
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False

        i = i - 1
        j = j - 1

    i = row - 1
    j = col - 1
    # Right Diagonl
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False

    # Left Down Diagonal
    i = row + 1
    j = col - 1
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i = i + 1
        j = j - 1

    i = row + 1
    j = col + 1

    while i < N and j < N:
        if board[i][j] == 1:
            return False
        i = i + 1
        j = j + 1

    return True


def solveNQUtil(col):
    if col >= N:
        return True

    for i in range(N):
        if isSafe(i, col):
            board[i][col] = 'Q'
            if solveNQUtil(col + 1) == True:
                return True

            board[i][col] = 0
    return False


getBoard()
solveNQUtil(0)
printBoard()