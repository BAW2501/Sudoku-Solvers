from BacktrakingSolver import *
from LppSolver import *

SUDOKU_SIZE: int = 9
board = [[1, 7, 4, 0, 9, 0, 6, 0, 0],
         [0, 0, 0, 0, 3, 8, 1, 5, 7],
         [5, 3, 0, 7, 0, 1, 0, 0, 4],
         [0, 0, 7, 3, 4, 9, 8, 0, 0],
         [8, 4, 0, 5, 0, 0, 3, 6, 0],
         [3, 0, 5, 0, 0, 6, 4, 7, 0],
         [2, 8, 6, 9, 0, 0, 0, 0, 1],
         [0, 0, 0, 6, 2, 7, 0, 3, 8],
         [0, 5, 3, 0, 8, 0, 0, 9, 6]]


def print_board(bo):
    for i in range(SUDOKU_SIZE):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(SUDOKU_SIZE):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


if __name__ == "__main__":
    board2 = list()
    board2.extend(board)
    print_board(board)
    print("\n\n\n")

    if backtrack_solver(board):
        print_board(board)
    else:
        print("no solution found")
    print("\n\n\n")
    if lpp_solver(board):
        print_board(board)
    else:
        print("no solution found")

