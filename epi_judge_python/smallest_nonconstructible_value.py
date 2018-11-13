from test_framework import generic_test


def smallest_nonconstructible_value(A):
    A.sort()
    res = 0
    for x in A:
        if x > res + 1:
            return res + 1
        else:
            res += x
    return res + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("smallest_nonconstructible_value.py",
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
