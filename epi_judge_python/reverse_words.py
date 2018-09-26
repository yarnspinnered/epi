import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a string encoded as bytearray.
def reverse_words(s):
    s.reverse()

    def my_reverse(start, end):
        while start < end:
            s[start], s[end - 1] = s[end - 1], s[start]
            start += 1
            end -= 1
    boundary = 0

    while True:
        i = s.find(b' ', boundary)
        if i < 0:
            break
        my_reverse(boundary, i)
        boundary = i + 1

    my_reverse(boundary, len(s))
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
