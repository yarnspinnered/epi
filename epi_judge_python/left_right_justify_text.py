from test_framework import generic_test


def justify_text(words, L):
    res, line, line_alphabet_count = [], [], 0
    for w in words:
        if line_alphabet_count + len(line) + len(w) <= L:
            line.append(w)
            line_alphabet_count += len(w)
        else:
            for i in range(L - line_alphabet_count):
                line[i % max(1, len(line) - 1)] += " "
            res.append("".join(line))
            line = [w]
            line_alphabet_count = len(w)

    last_line = " ".join(line)
    res.append(last_line + " " * (L - len(last_line)))

    return res

justify_text(["Listen", "to", "many,", "speak", "to", "a", "few."], 6)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("left_right_justify_text.py",
                                       'left_right_justify_text.tsv',
                                       justify_text))
