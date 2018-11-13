from test_framework import generic_test


def matrix_search(A, x):
    i, j = 0, len(A[0]) - 1

    while 0 <= i < len(A) and 0 <= j < len(A[i]):
        v = A[i][j]
        if v == x:
            return True
        elif v < x:
            i += 1
        else:
            j -= 1

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_row_col_sorted_matrix.py",
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
