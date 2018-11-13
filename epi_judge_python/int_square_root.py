from test_framework import generic_test


def square_root(k):
    l, r = 0, 2 ** 16

    while l <= r:
        m = (l + r)//2
        if m ** 2 <= k and (m + 1) ** 2 > k:
            return m
        elif m ** 2 < k:
            l = m + 1
        else:
            r = m - 1
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
