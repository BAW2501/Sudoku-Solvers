from pulp import *

SUDOKU_SIZE: int = 9
"""
this problem can be modeled as a linear programing problem like
x_ijk mean that cell i,j is set to value k

max z= 0
such that
sum(x_ijk,i=1..9)==1 for j, k= 1..9 // (1) this is to ensure that value k appears only once in line i
sum(x_ijk,j=1..9)==1 for i, k= 1..9 // (2) this is to ensure that value k appears only once in column j
sum(x_ijk,k=1..9)==1 for i, j= 1..9 // (3)
sum(sum(x_ijk,k=3q-2..3q),r=3p-2..3p)==1 for i=1..9 and p,q=1..3

reference http://profs.sci.univr.it/~rrizzi/classes/PLS2015/sudoku/doc/497_Olszowy_Wiktor_Sudoku.pdf
"""


# https://www.coin-or.org/PuLP/CaseStudies/a_sudoku_problem.html


# A list of strings from "1" to "9" is created
def lpp_solver(board):
    sequence = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # The Vals, Rows and Cols sequences all follow this form
    vals = sequence
    rows = sequence
    cols = sequence

    # The boxes list is created, with the row and column index of each square in each box
    boxes = []
    for i in range(3):
        for j in range(3):
            boxes += [[(rows[3 * i + k], cols[3 * j + s]) for k in range(3) for s in range(3)]]

    # The prob variable is created to contain the problem data
    prob = LpProblem("Sudoku_Problem", LpMinimize)

    # The problem variables are created
    choices = LpVariable.dicts("Choice", (vals, rows, cols), 0, 1, LpBinary)

    # The arbitrary objective function is added
    prob += 0, "Arbitrary Objective Function"

    # A constraint ensuring that only one value can be in each square is created
    for r in rows:
        for c in cols:
            prob += lpSum([choices[v][r][c] for v in vals]) == 1, ""

    # The row, column and box constraints are added for each value
    for v in vals:
        for r in rows:
            prob += lpSum([choices[v][r][c] for c in cols]) == 1, ""

        for c in cols:
            prob += lpSum([choices[v][r][c] for r in rows]) == 1, ""

        for b in boxes:
            prob += lpSum([choices[v][r][c] for (r, c) in b]) == 1, ""

    # The starting numbers are entered as constraints
    for i in range(SUDOKU_SIZE):
        for j in range(SUDOKU_SIZE):
            if board[i][j] != 0:
                prob += choices[f"{board[i][j]}"][f"{i+1}"][f"{j+1}"] == 1, ""

    # The problem is solved using PuLP's choice of Solver
    prob.solve(PULP_CBC_CMD(msg=False))

    for r in rows:
        for c in cols:
            for v in vals:
                if value(choices[v][r][c]) == 1:
                    board[int(r)-1][int(c)-1] = int(v)

    return True
