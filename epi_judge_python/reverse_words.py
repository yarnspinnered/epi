import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a string encoded as bytearray.
def reverse_words(s):
    def myReverse(start, end):
        l, r = start, end
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    myReverse(0, len(s) - 1)

    i = 0
    for j in range(len(s)):
        if s[j] == ord(" "):
            myReverse(i, j - 1)
            i = j + 1

    myReverse(i, len(s) - 1)
    return

@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
