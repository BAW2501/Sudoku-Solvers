SUDOKU_SIZE: int = 9
def find_empty(bo):
    for i in range(SUDOKU_SIZE):
        for j in range(SUDOKU_SIZE):
            if bo[i][j] == 0:
                return i, j
    return -1, -1


def is_valid(puzzle, row, column, guess):
    corner_x = row // 3 * 3
    corner_y = column // 3 * 3

    for x in range(SUDOKU_SIZE):
        if puzzle[row][x] == guess:
            return False
        if puzzle[x][column] == guess:
            return False
        if puzzle[corner_x + (x % 3)][corner_y + (x // 3)] == guess:
            return False

    return True


def backtrack_solver(bo):
    i, j = find_empty(bo)

    if i == -1:
        return True

    for num in range(1, 10):
        if is_valid(bo, i, j, num):
            bo[i][j] = num
            if backtrack_solver(bo):
                return True
            bo[i][j] = 0
