from test_framework import generic_test


def search_first_of_k(A, k):
    l, r = 0, len(A) - 1

    curr = -1
    while l <= r:
        m = (l + r)//2
        if A[m] == k:
            curr = m
            r = m - 1
        elif A[m] < k:
            l = m + 1
        else:
            r = m - 1

    return curr


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
