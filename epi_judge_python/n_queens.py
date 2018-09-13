from test_framework import generic_test


def n_queens(n):
    def helper(row):
        if row == n:
            res.append(list(col_placement))
            return

        for j in range(n):
            if all(j != c for c in col_placement[:row]) and \
                all(abs(row - i) != abs(j - c) for i,c in enumerate(col_placement[:row])):
                col_placement[row] = j
                helper(row + 1)

    res, col_placement = [],[-1] * n
    helper(0)

    return res


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("n_queens.py", 'n_queens.tsv', n_queens,
                                       comp))
