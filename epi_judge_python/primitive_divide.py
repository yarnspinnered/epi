from test_framework import generic_test


def divide(x, y):
    result, i = 0, 0
    xtmp, power = x, 32 - 1

    while power >= 0:
        if xtmp >= (y << power):
            xtmp -= (y << power)
            result |= 1
        power -= 1
        result <<= 1
    print(bin(result))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("primitive_divide.py",
                                       "primitive_divide.tsv", divide))
