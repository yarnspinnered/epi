from test_framework import generic_test


def justify_text(words, L):
    res, curr_str, curr_str_len = [], [], 0

    for w in words:
        if curr_str_len + len(w) + len(curr_str) > L:
            for i in range(L - curr_str_len):
                curr_str[i % max(len(curr_str) - 1, 1)] += " "
            res.append("".join(curr_str))
            curr_str = []
            curr_str_len = 0
        curr_str.append(w)
        curr_str_len += len(w)

    return res + [" ".join(curr_str).ljust(L)]

    return res
justify_text(["Listen", "to", "many,", "speak", "to", "a", "few."], 6)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("left_right_justify_text.py",
                                       'left_right_justify_text.tsv',
                                       justify_text))
