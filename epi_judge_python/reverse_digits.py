from test_framework import generic_test


def reverse(x):
    negative = False
    if x < 0:
        negative = True
        x *= -1
    res = 0

    while x:
        res += x % 10
        x //= 10
        if x >0 :
            res *= 10

    if negative:
        res *= -1
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))
