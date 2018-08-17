from test_framework import generic_test
from test_framework.test_failure import TestFailure
import functools

def int_to_string(x):
    # TODO - you fill in here.
    neg = False
    if x < 0:
        x = -x
        neg = True
    res = ""
    while True:
        res = chr(ord('0') + (x % 10)) + res
        x = x // 10
        if x == 0:
            break
    if neg:
        res = '-' + res
    return res


def string_to_int(s):
    # TODO - you fill in here.
    # res = 0
    # neg = False
    # if s[0] == '-':
    #     neg = True
    #     s = s[1:]
    # for i,c in enumerate(reversed(s)):
    #     res += (ord(c) - ord('0')) * 10 ** i
    # if neg:
    #     res *= -1
    res = functools.reduce(lambda acc,x: acc * 10 + (ord(x)-ord('0')) ,s[(s[0]=='-'):],0)
    return res * (-1 if s[0] == '-' else 1)


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
