from test_framework import generic_test
from collections import deque
import string
# Uses BFS to find the least steps of transformation.
# dictionary method
# def transform_string(D, s, t):
#     def check_adjacent(a,b):
#         if len(a) != len(b) or a == b:
#             return False
#         diff = 0
#         i = 0
#         while i < len(a) and diff <= 1:
#             if a[i] != b[i]:
#                 diff += 1
#             i += 1
#         return diff <= 1
#
#     q = deque([(0,s)])
#     explored = {s}
#
#     while q:
#         steps, curr = q.pop()
#         if curr == t:
#             return steps
#         for w in D:
#             if check_adjacent(w, curr) and w not in explored:
#                 explored.add(w)
#                 q.appendleft((steps + 1, w))
#
#
#     return -1

def transform_string(D, s, t):
    def check_adjacent(a,b):
        if len(a) != len(b) or a == b:
            return False
        diff = 0
        i = 0
        while i < len(a) and diff <= 1:
            if a[i] != b[i]:
                diff += 1
            i += 1
        return diff <= 1

    q = deque([(0,s)])
    explored = {s}

    while q:
        steps, curr = q.pop()
        if curr == t:
            return steps
        for i in range(len(curr)):
            for c in string.ascii_lowercase:
                w = curr[0:i] + c + curr[i + 1:]
                if w in D and w not in explored:
                    explored.add(w)
                    q.appendleft((steps + 1, w))


    return -1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_transformability.py",
                                       'string_transformability.tsv',
                                       transform_string))
