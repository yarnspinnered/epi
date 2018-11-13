from test_framework import generic_test


def swap_bits(x, i, j):
    bit_i = 1 << i
    bit_j = 1 << j
    if (x & bit_i) >> i != (x & bit_j) >> j :
        mask = bit_i | bit_j
        x ^= mask
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("swap_bits.py", 'swap_bits.tsv',
                                       swap_bits))
