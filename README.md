Sudoku as CSP
=============

# Introduction
This simple code contains the solution of Sudoku game exploiting AIMA csp [implementation](https://github.com/aimacode/aima-python).

# Requirements

 - wget or git
 - unzip
 - python 3.x

# How to get
## Via wget
```
wget https://github.com/buele/sudoku-csp/archive/master.zip
unzip sudoku-csp-master.zip
```

## Via git
```
git clone https://github.com/buele/sudoku-csp.git
```

# How to run
The run.py script accept an argument for the sudoku grid definition
Sudoku grid sample:

```
...26.7.168..7..9.19...45..82.1...4...46.29...5...3.28..93...74.4..5..367.3.18...
```
That represents the following grid:

```
|-----------------------------|
| *  *  * | 2  6  * | 7  *  1 |
| 6  8  * | *  7  * | *  9  * |
| 1  9  * | *  *  4 | 5  *  * |
|-----------------------------|
| 8  2  * | 1  *  * | *  4  * |
| *  *  4 | 6  *  2 | 9  *  * |
| *  5  * | *  *  3 | *  2  8 |
|-----------------------------|
| *  *  9 | 3  *  * | *  7  4 |
| *  4  * | *  5  * | *  3  6 |
| 7  *  3 | *  1  8 | *  *  * |
|-----------------------------|
```

Where the '*' chars means the empty cells.

So to run the sudoku solver:

```
cd sudoku-csp
python3 run.py "...26.7.168..7..9.19...45..82.1...4...46.29...5...3.28..93...74.4..5..367.3.18..."

```
Output:

```
|-----------------------------|
| 4  3  5 | 2  6  9 | 7  8  1 |
| 6  8  2 | 5  7  1 | 4  9  3 |
| 1  9  7 | 8  3  4 | 5  6  2 |
|-----------------------------|
| 8  2  6 | 1  9  5 | 3  4  7 |
| 3  7  4 | 6  8  2 | 9  1  5 |
| 9  5  1 | 7  4  3 | 6  2  8 |
|-----------------------------|
| 5  1  9 | 3  2  6 | 8  7  4 |
| 2  4  8 | 9  5  7 | 1  3  6 |
| 7  6  3 | 4  1  8 | 2  5  9 |
|-----------------------------|
```




# Credits
The files csp.py, search.py, utils.py are from the aima-python repository.
The implementation of Sudoku (sudoku.py) as CSP is written by Raffaele Bua.
