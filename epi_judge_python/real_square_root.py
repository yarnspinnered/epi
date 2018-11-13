from test_framework import generic_test
import math

def square_root(x):
    l, r = (0, x) if x >= 1 else (x, 1)

    while not math.isclose(l,r):
        m = (l + r)/2
        if m ** 2 < x:
            l = m
        else:
            r = m
    return l



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("real_square_root.py",
                                       'real_square_root.tsv', square_root))
