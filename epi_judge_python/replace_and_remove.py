import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    relevant = 0
    a_cnt = 0
    for i in range(size):
        if s[i] == 'b':
            s[i] = ''
        else:
            if s[i] == 'a':
                a_cnt += 1
            s[relevant] = s[i]
            relevant += 1

    new_iter = relevant - 1 + a_cnt
    old_iter = relevant - 1
    while old_iter >= 0:
        if s[old_iter] == 'a':
            s[new_iter], s[new_iter - 1] = 'd', 'd'
            new_iter -= 2
        else:
            s[new_iter] = s[old_iter]
            new_iter -= 1
        old_iter -= 1

    return relevant+a_cnt

@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
