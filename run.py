from sudoku import Sudoku

from csp import AC3

example = "...26.7.168..7..9.19...45..82.1...4...46.29...5...3.28..93...74.4..5..367.3.18..."

e = Sudoku(example)
e.display(e.infer_assignment())
AC3(e)
e.display(e.infer_assignment())
