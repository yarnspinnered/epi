from test_framework import generic_test


def majority_search(stream):
    curr_count = 0
    curr_char = None

    for x in stream:
        if curr_count == 0:
            curr_char = x
            curr_count = 1
        else:
            if curr_char == x:
                curr_count += 1
            else:
                curr_count -= 1
    return curr_char


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("majority_element.py",
                                       'majority_element.tsv',
                                       majority_search_wrapper))
