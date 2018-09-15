from test_framework import generic_test


def find_nearest_repetition(paragraph):
    d = {}
    for i,w in enumerate(paragraph):
        d.setdefault(w, []).append(i)
    smallest = float('inf')
    smallest_word = None

    for k,v in d.items():
        for i in range(len(v) - 1):
            dist = v[i+1] - v[i]
            if dist < smallest:
                smallest = dist
                smallest_word = k

    if smallest == float('inf'):
        return -1
    else:
        return smallest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
