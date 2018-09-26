from test_framework import generic_test
from collections import Counter

# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):
    for row in partial_assignment:
        if any((x > 1) for c,x in Counter(row).items() if c != 0):
            return False

    for col in range(len(partial_assignment)):
        column = Counter(partial_assignment[i][col] for i in range(len(partial_assignment)))
        if any((x > 1) for c, x in column.items() if c != 0):
            return False

    for x in range(3):
        for y in range(3):
            region = (partial_assignment[i + x * 3][j + y * 3] for i in range(3) for j in range(3))
            if any(x > 1 for c, x in Counter(region).items() if c != 0):
                return False

    return True



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
