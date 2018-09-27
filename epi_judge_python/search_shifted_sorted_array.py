from test_framework import generic_test


def search_smallest(A):
    def helper(l, r):
        m = (l + r)//2
        if m == l:
            return m if A[m] <= A[r] else r
        elif m == r:
            return m if A[m] <= A[l] else l

        if A[l] <= A[m] and A[m] <= A[r]:
            return m if A[m] <= A[l] else l
        elif A[l] > A[m]:
            return helper(l, m)
        else:
            return helper(m, r)

    return helper(0, len(A) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
