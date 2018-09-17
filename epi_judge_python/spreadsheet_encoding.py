from test_framework import generic_test


def ss_decode_col_id(col):
    tot = 0
    for c in col:
        tot = tot * 26 + (ord(c) - ord('A') + 1)


    return tot


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spreadsheet_encoding.py",
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
