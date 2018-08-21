from test_framework import generic_test


def binary_search_unknown_length(A, k):
    if not A:
        return -1
    end = 1
    while True:
        try:
            if A[end - 1] == k:
                return end - 1
            elif A[end - 1] < k:
                end = end * 2
            else:
                break
        except IndexError:
            break
    l = end  // 2
    r = (end - 1)


    while l <= r:
        m = l + (r - l)// 2
        try:
            if A[m] == k:
                return m
            elif A[m] < k:
                l = m + 1
            elif A[m] > k:
                r = m - 1
        except:
            r = m - 1

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_unknown_length_array.py",
                                       'search_unknown_length_array.tsv',
                                       binary_search_unknown_length))
