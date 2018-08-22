from test_framework import generic_test


def gcd(x, y):
    if x < y:
        return gcd(y,x)
    elif y == 0:
        return x
    elif x & 1 == 0 and y & 1 == 0:
        return gcd(x >> 1, y >> 1) << 1
    elif x & 1 == 0 and y & 1 == 1:
        return gcd(x >> 1, y)
    elif x & 1 == 1 and y & 1 == 0:
        return gcd(x, y >> 1)
    else:
        return gcd(x - y, y)



if __name__ == '__main__':
    exit(generic_test.generic_test_main("gcd.py", 'gcd.tsv', gcd))
