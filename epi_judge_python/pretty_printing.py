from test_framework import generic_test
import functools
from operator import add, itemgetter

def minimum_messiness(words, line_length):
    def messiness(one_line):
        return (line_length - len(' '.join(one_line)))**2

    prefix = []

    for i in range(len(words)):
        candidates = []
        j = i
        while j >= 0 and len(' '.join(words[j:i + 1])) <= line_length :
            if j == 0:
                candidates.append(messiness(words[j:i + 1]))
            else:
                candidates.append(prefix[j - 1] + messiness(words[j:i + 1]))
            j -= 1

        prefix.append(min(candidates))

    return prefix[len(words) - 1]

minimum_messiness(["aaa", "bbb", "c", "d", "ee", "ff", "gggggg"], 11)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "pretty_printing.py", 'pretty_printing.tsv', minimum_messiness))
