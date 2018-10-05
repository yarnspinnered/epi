
from test_framework import generic_test
cache = []
for i in range(2 ** 16):
    curr = i
    for j in range(8):
        right_end = (i >> j) & 1
        left_end = (i >> (16 - j)) & 1
        if right_end != left_end:
            bit_mask = (1 << j) | (1 << (16 - j))
            curr ^= bit_mask
    cache.append(curr)

def reverse_bits(x):
    end = 0xFFFF

    print('start: ', bin(x))
    res = 0
    for i in range(4):
        print(bin(res))
        curr = 0xFFFF & (x >> ( 16 * (3 - i)))
        res |= (cache[curr] << (16 * i))
    print('my answer: ', bin(res))
    print(bin(res))
    return res >> 1
print(reverse_bits(123))
# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv",
#                                        reverse_bits))
