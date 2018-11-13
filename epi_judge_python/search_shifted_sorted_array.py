from test_framework import generic_test


def search_smallest(A):
    l,r = 0, len(A) - 1
    res = -1
    while l <= r:
        m = (l + r)//2
        if A[0] <= A[m] and (m == len(A) - 1 or A[m + 1] < A[m]):
            res = m
            break
        elif A[0] <= A[m]:
            l = m + 1
        else:
            r = m -1

    return 0 if res == len(A) - 1 else m + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
