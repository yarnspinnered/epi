from test_framework import generic_test


def gcd(x, y):
    def is_even(x):
        return x & 1 == 0

    if x == 0:
        return y
    elif y == 0:
        return x
    elif x == y:
        return x

    if x > y:
        big = x
        small = y
    else:
        big = y
        small = x

    if is_even(big) and is_even(small):
        return gcd(big >> 1, small >> 1) << 1
    elif not is_even(big) and not is_even(small):
        return gcd(big - small, small)
    elif is_even(big) and not is_even(small):
        return gcd(big >> 1, small)
    else:
        return gcd(big, small >> 1)



if __name__ == '__main__':
    exit(generic_test.generic_test_main("gcd.py", 'gcd.tsv', gcd))
