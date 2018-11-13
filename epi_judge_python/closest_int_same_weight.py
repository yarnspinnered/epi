from test_framework import generic_test


def closest_int_same_bit_count(x):
    for i in range(64):
        left_mask = (1 << i)
        right_mask = (1 << (i + 1))

        if (x & left_mask) >> i !=  (x & right_mask) >> (i + 1):
            combined = left_mask | right_mask
            return x ^ combined
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("closest_int_same_weight.py",
                                       "closest_int_same_weight.tsv",
                                       closest_int_same_bit_count))
