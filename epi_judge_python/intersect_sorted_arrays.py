from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    res = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        a = A[i]
        b = B[j]
        if a < b:
            i += 1
        elif a > b:
            j += 1
        else:
            i += 1
            j += 1
            if len(res) == 0 or res[-1] != b:
                res.append(b)

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
