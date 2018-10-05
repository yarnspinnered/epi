from test_framework import generic_test


def roman_to_integer(s):
    i = 0
    res = 0
    m = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    while i < len(s):
        if i == len(s) - 1:
            res += m[s[i]]
            i += 1
            continue
        if s[i:i+2] in set(["IV","IX", "XL", "XC", "CD", "CM"]):
            res = res - m[s[i]] + m[s[i + 1]]
            i += 2
        else:
            res += m[s[i]]
            i += 1
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", 'roman_to_integer.tsv', roman_to_integer))
