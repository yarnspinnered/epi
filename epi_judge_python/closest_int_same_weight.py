from test_framework import generic_test


def closest_int_same_bit_count(x):
    smallest_0 = None
    smallest_1 = None

    for i in range(64):
        current = x >> i & 1
        if current == 0:
            smallest_0 = i
        else:
            smallest_1 = i
        if not smallest_0 is None and not smallest_1 is None:
            BIT_MASK = (1 << smallest_0) | (1 << smallest_1)
            return x ^ BIT_MASK
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("closest_int_same_weight.py",
                                       "closest_int_same_weight.tsv",
                                       closest_int_same_bit_count))
