from test_framework import generic_test
import string
import functools
def convert_base(num_as_string, b1, b2):
    num_as_string = num_as_string.lower()

    i = 0

    is_zero = False
    if num_as_string == "0" or num_as_string == "-0":
        return num_as_string

    is_negative = False
    if num_as_string[0] == '-':
        is_negative = True
        i += 1

    d = dict(zip(string.hexdigits[:16], range(16)))
    interm = 0
    while i < len(num_as_string):
        interm *= b1
        interm += d[num_as_string[i]]
        i += 1

    res = ""
    while interm > 0:
        v = interm % b2
        interm //= b2
        res = string.hexdigits[v] + res
    return ('-' if is_negative else '') + ("0" if is_zero else '')+res.upper()

convert_base('511288644', 10, 3)
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
