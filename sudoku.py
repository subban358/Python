def printFileBoard(board):
    string = ""
    string = string + "*********************\n"
    for x in range(0, 9):
        if x == 3 or x == 6:
            string = string + "*********************\n"
        for y in range(0, 9):
            if y == 3 or y == 6:
                string = string + " * "
            string = string + str(board[x][y]) + " "
        string = string + "\n"
    string = string + "*********************\n"
    return string


# function to print the board on to the console
def printBoard(board):
    print("*********************")
    for x in range(0, 9):
        if x == 3 or x == 6:
            print("*********************")
        for y in range(0, 9):
            if y == 3 or y == 6:
                print("*", end=" ")
            print(board[x][y], end=" ")
        print()
    print("*********************")


# function to check if the board is full or not
# returns true if it is full and false if it isn't
# it works on the fact that if it finds at least one
# zero in the board it returns false
def isFull(board):
    for x in range(0, 9):
        for y in range(0, 9):
            if board[x][y] == 0:
                return False
    return True


# function to find all of the possible numbers
# which can be put at the specifies location by
# checking the horizontal and vertical and the
# three by three square in which the numbers are
# housed
def possibleEntries(board, i, j):
    possibilityArray = {}

    for x in range(1, 10):
        possibilityArray[x] = 0

    # For horizontal entries
    for y in range(0, 9):
        if not board[i][y] == 0:
            possibilityArray[board[i][y]] = 1

    # For vertical entries
    for x in range(0, 9):
        if not board[x][j] == 0:
            possibilityArray[board[x][j]] = 1

    # For squares of three x three
    k = 0
    l = 0
    if 0 <= i <= 2:
        k = 0
    elif 3 <= i <= 5:
        k = 3
    else:
        k = 6
    if 0 <= j <= 2:
        l = 0
    elif 3 <= j <= 5:
        l = 3
    else:
        l = 6
    for x in range(k, k + 3):
        for y in range(l, l + 3):
            if not board[x][y] == 0:
                possibilityArray[board[x][y]] = 1

    for x in range(1, 10):
        if possibilityArray[x] == 0:
            possibilityArray[x] = x
        else:
            possibilityArray[x] = 0

    return possibilityArray


# recursive function which solved the board and
# prints it.
def sudokuSolver(board):
    i = 0
    j = 0

    possiblities = {}

    # if board is full, there is no need to solve it any further
    if isFull(board):
        print("Board Solved Successfully!")
        printBoard(board)
        return
    else:
        # find the first vacant spot
        for x in range(0, 9):
            for y in range(0, 9):
                if board[x][y] == 0:
                    i = x
                    j = y
                    break
            else:
                continue
            break

        # get all the possibilities for i,j
        possiblities = possibleEntries(board, i, j)

        # go through all the possibilities and call the the function
        # again and again
        for x in range(1, 10):
            if possiblities[x] != 0:
                board[i][j] = possiblities[x]
                sudokuSolver(board)
        # backtrack
        board[i][j] = 0


def main():
    SudokuBoard = [[0, 0, 0, 3, 0, 0, 2, 0, 0],
                   [0, 0, 0, 0, 0, 8, 0, 0, 0],
                   [0, 7, 8, 0, 6, 0, 3, 4, 0],
                   [0, 4, 2, 5, 1, 0, 0, 0, 0],
                   [1, 0, 6, 0, 0, 0, 4, 0, 9],
                   [0, 0, 0, 0, 8, 6, 1, 5, 0],
                   [0, 3, 5, 0, 9, 0, 7, 6, 0],
                   [0, 0, 0, 7, 0, 0, 0, 0, 0],
                   [0, 0, 9, 0, 0, 5, 0, 0, 0]
                   ]
    printBoard(SudokuBoard)
    sudokuSolver(SudokuBoard)


if __name__ == "__main__":
    main()
