from test_framework import generic_test
from collections import Counter

def is_letter_constructible_from_magazine(letter_text, magazine_text):
    letter_d = Counter(letter_text)
    magazine_d = Counter(magazine_text)

    for k,v in letter_d.items():
        if magazine_d.get(k,0) < v:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
