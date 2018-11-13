from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    res = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
        else:
            res.append(A[i])
            while i < len(A) and A[i] == B[j]:
                i += 1
            if i >= len(A):
                break
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
