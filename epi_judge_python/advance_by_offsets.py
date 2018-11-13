from test_framework import generic_test


def can_reach_end(A):
    i, furthest = 0, 0

    while i <= furthest and i < len(A):
        furthest = max(A[i] + i, furthest)
        i += 1

    return furthest >= len(A) - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
