from test_framework import generic_test
from collections import Counter

def can_form_palindrome(s):
    c = Counter(s)
    num_odds = 0
    for i,v in c.items():
        if v % 2 == 1:
            num_odds += 1

    return num_odds < 2


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
