from test_framework import generic_test
from string import ascii_uppercase

def ss_decode_col_id(col):
    tot = 0
    for c in col:
        tot = tot * 26 + ( 1 + ascii_uppercase.index(c))

    return tot


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spreadsheet_encoding.py",
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
