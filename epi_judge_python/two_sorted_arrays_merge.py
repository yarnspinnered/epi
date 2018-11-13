from test_framework import generic_test


def merge_two_sorted_arrays(A, m, B, n):
    A[-m:] = A[:m]
    i = len(A) - m
    j,m = 0,0

    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            A[m] = A[i]
            i += 1
        else:
            A[m] = B[j]
            j += 1
        m += 1
    if i == len(A):
        A[m:] = B[j:]

    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
