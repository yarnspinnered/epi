import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a string encoded as bytearray.
def reverse_words(s):
    s.reverse()


    def reverse_range(l,r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    start, i = 0, 0
    while i < len(s):
        if s[i] == ord(' '):
            reverse_range(start, i - 1)
            start = i + 1
        i += 1
    reverse_range(start, i - 1)

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
