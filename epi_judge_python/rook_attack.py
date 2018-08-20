import copy

from test_framework import generic_test


def rook_attack(A):

    # def mark_row_for_change(A, i):
    #     for j,x in enumerate(A[i]):
    #         if x != 0 and x != "aaa":
    #             A[i][j] = "aaa"
    #
    # def mark_col_for_change(A,j):
    #     for i in range(len(A)):
    #         if A[i][j] != 0 and A[i][j] != "aaa":
    #             A[i][j] = "aaa"
    #
    # for i in range(len(A)):
    #     for j in range(len(A[i])):
    #         if A[i][j] == 0:
    #             print("HIT: ", i, j)
    #             mark_col_for_change(A, j)
    #             mark_row_for_change(A, i)
    #
    # print("after marking: ", A)
    # for i in range(len(A)):
    #     for j in range(len(A[i])):
    #         if A[i][j] == "aaa":
    #             A[i][j] = 0

    change_first_row = 0 in A[0]
    change_first_col = False
    for row in A:
        if row[0] == 0:
            change_first_col = True

    for i in range(1, len(A)):
        for j in range(1, len(A[i])):
            if A[i][j] == 0:
                A[i][0] = 0
                A[0][j] = 0


    for i in range(1, len(A)):
        for j in range(1, len(A[i])):
            if A[i][0] == 0 or A[0][j] == 0:
                A[i][j] = 0

    for j in range(len(A[0])):
        if change_first_row:
            A[0][j] = 0

    for i in range(len(A)):
        if change_first_col:
            A[i][0] = 0

    return


def rook_attack_wrapper(A):
    a_copy = copy.deepcopy(A)
    rook_attack(a_copy)
    return a_copy


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("rook_attack.py", 'rook_attack.tsv',
                                       rook_attack_wrapper))
