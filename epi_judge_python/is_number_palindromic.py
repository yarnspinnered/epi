from test_framework import generic_test
import math

def is_palindrome_number(x):
    if x < 0:
        return False
    if x == 0:
        return True

    length = math.ceil(math.log(x, 10)) if (math.ceil(math.log(x, 10)) - math.log(x, 10)) < 0.0000005 else math.floor(math.log(x, 10))
    base = 0

    while length > base:
        if (x // 10 ** length) % 10 != (x // 10 ** base) % 10:
            return False
        length -= 1
        base += 1

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
