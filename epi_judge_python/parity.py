from test_framework import generic_test


def par(n):
    ones = 0
    while n > 0:
        n &= n - 1
        ones ^= 1
    return ones

cache = [0 for _ in range(2 ** 16)]
for i in range(2 ** 16):
    cache[i] = par(i)

def parity(x):
    pars = 0
    for i in range(4):
        if pars == 1 and cache[(x >> 16 * i) & 0xFFFF] == 1:
            pars = 0
        elif pars == 0 and cache[(x >> 16 * i) & 0xFFFF] == 0:
            pars = 0
        else:
            pars = 1
    return pars


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
