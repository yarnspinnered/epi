from test_framework import generic_test, test_utils
from collections import defaultdict

def find_anagrams(dictionary):
    d = defaultdict(list)
    for w in dictionary:
        d["".join(sorted(w)).strip()].append(w)
    return list(x for x in d.values() if len(x) >= 2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "anagrams.py",
            "anagrams.tsv",
            find_anagrams,
            comparator=test_utils.unordered_compare))
