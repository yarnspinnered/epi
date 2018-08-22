import copy

from test_framework import generic_test


def rook_attack(A):

    if not A:
        return A
    first_row_attacked = 0 in A[0]
    first_col_attacked = 0 in [x[0] for x in A]

    for i in range(1, len(A)):
        for j in range(1, len(A[0])):
            if A[i][j] == 0:
                A[i][0] = 0
                A[0][j] = 0

    for j in range(1, len(A[0])):
        if A[0][j] == 0:
            for i in range(1, len(A)):
                A[i][j] = 0

    for i in range(1, len(A)):
        if A[i][0] == 0:
            for j in range(1, len(A[0])):
                A[i][j] = 0

    if first_col_attacked:
        for i in range(len(A)):
            A[i][0] = 0

    if first_row_attacked:
        for j in range(len(A[0])):
            A[0][j] = 0

    return


def rook_attack_wrapper(A):
    a_copy = copy.deepcopy(A)
    rook_attack(a_copy)
    return a_copy


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("rook_attack.py", 'rook_attack.tsv',
                                       rook_attack_wrapper))
