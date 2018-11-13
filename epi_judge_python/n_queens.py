from test_framework import generic_test


def n_queens(n):
    def helper(row):
        if row == n:
            res.append(list(col_placement))
            return
        for c in range(n):
            if all(abs(c-existing_c) not in (0, abs(row - i))
                   for i,existing_c in enumerate(col_placement[:row])):
                col_placement[row] = c
                helper(row + 1)
    res, col_placement = [], [0] * n
    helper(0)
    return res


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("n_queens.py", 'n_queens.tsv', n_queens,
                                       comp))
