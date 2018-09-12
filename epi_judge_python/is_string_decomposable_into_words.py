import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import encommentsable_executor_hook


def decompose_into_dictionary_words(domain, dictionary):
    # TODO - you fill in here.
    indexes = [-1 for x in range(len(domain) + 1)]
    indexes[0] = 0

    for i in range(1, len(domain) + 1):
        for w in dictionary:
            if domain[(i - len(w)):i] == w and indexes[i - len(w)] != -1:
                indexes[i] = i - len(w)
    res = []
    if indexes[len(domain)] != -1:
        i = len(domain)

        while i > 0:
            idx = indexes[i]
            res.append(domain[idx:i])
            i = idx
    res = res[::-1]
    print("result: " + str(res))
    return res

decompose_into_dictionary_words("ja", ['a', 'j'])

@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_decomposable_into_words.py",
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
