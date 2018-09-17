from test_framework import generic_test
import string
import functools
def convert_base(num_as_string, b1, b2):
    def build_from_int(num):
        if num == 0:
            return ''
        return (build_from_int(num//b2) + string.hexdigits[num % b2].upper())

    is_negative = 1 if num_as_string[0] == '-' else 0
    num_as_int = functools.reduce(lambda acc, x: acc * b1 + string.hexdigits.index(x.lower()),
                                  num_as_string[is_negative:], 0)

    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else '') + build_from_int(num_as_int)

convert_base('511288644', 10, 3)
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
