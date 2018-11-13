from test_framework import generic_test


def power(x, y):
    result, pow = 1, y
    if y < 0:
        pow, x = -pow, 1.0 / x

    while pow:
        if pow & 1:
            pow -= 1
            result *= x
        else:
            pow >>= 1
            x *= x
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
