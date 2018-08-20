from test_framework import generic_test


def longest_matching_parentheses(s):
    bad, stack, longest = -1, [], 0

    for i,x in enumerate(s):
        if x == '(':
            stack.append(i)
        elif not stack:
            bad = i
        else:
            left_end = stack.pop()
            longest = max(longest, i - (stack[-1] if stack else bad))

    return longest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_substring_with_matching_parentheses.py",
            'longest_substring_with_matching_parentheses.tsv',
            longest_matching_parentheses))
