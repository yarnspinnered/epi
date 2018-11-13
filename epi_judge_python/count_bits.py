from test_framework import generic_test


def count_bits(x):
    if x < 0:
        x += 2 ** 32
    cnt = 0
    while x:
        x &= (x - 1)
        cnt += 1
    return cnt


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("count_bits.py", 'count_bits.tsv',
                                       count_bits))
