from test_framework import generic_test


def fibonacci(n):
    f = 0
    s = 1

    if n <= 1:
        return n
    else:
        for i in range(2,n + 1):
            tmp = f
            f = s
            s += tmp

    return s


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("fibonacci.py", 'fibonacci.tsv',
                                       fibonacci))
