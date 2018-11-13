import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(domain, dictionary):
    cache = [False for _ in range(len(domain) + 1)]
    cache[0] = True
    decompositions = [[] for _ in range(len(domain) + 1)]
    for j in range(1, len(domain) + 1):
        for i in range(j):
            if domain[i:j] in dictionary and (i == 0 or cache[i]):
                decompositions[j] = decompositions[i] + [domain[i:j]]
                cache[j] = True
                break

    return False if cache[-1] == False else decompositions[-1]

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
