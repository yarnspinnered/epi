from test_framework import generic_test
from collections import deque

# def is_pattern_contained_in_grid(grid, S):
#     def DFS(i, j, offset):
#         if offset == len(S):
#             return True
#         if (i,j,offset) in cache:
#             return False
#         dirs = []
#         flag = False
#
#
#         if i - 1 >= 0 and grid[i - 1][j] == S[offset]:
#             dirs.append((i - 1, j))
#         if i + 1 < height and grid[i + 1][j] == S[offset]:
#             dirs.append((i + 1, j))
#         if j - 1 >= 0 and grid[i][j - 1] == S[offset]:
#             dirs.append((i, j - 1))
#         if j + 1 < width and grid[i][j + 1] == S[offset]:
#             dirs.append((i, j + 1))
#         for step in dirs:
#             explored.add(step)
#             flag = flag or DFS(step[0], step[1], offset + 1)
#         if not flag:
#             cache.add((i,j, offset))
#         return flag
#
#     if not S:
#         return True
#     if not grid:
#         return False
#
#     start = S[0]
#     q = deque()
#     height = len(grid)
#     width = len(grid[0])
#     cache = set()
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j] == start:
#                 q.append((i,j))
#
#
#     while q:
#         i,j = q.pop()
#         offset = 1
#         explored = set([i, j])
#         if DFS(i, j, offset):
#             return True
#
#
#     return False

def is_pattern_contained_in_grid(grid, S):
    def dfs(i, j, offset):
        if offset == len(S):
            return True
        if (i,j,offset) in cache:
            return False
        if 0 <= i < len(grid) \
            and 0 <= j < len(grid[i]) \
            and grid[i][j] == S[offset] \
            and any(dfs(i+a, j + b, offset + 1) for a,b in [(-1, 0), (1, 0), (0, -1), (0, 1)]):
                return True

        cache.add((i,j, offset))
        return False

    cache = set()

    return any(dfs(i,j,0) for i in range(len(grid)) for j in range(len(grid[i])))
is_pattern_contained_in_grid([[8, 11, 10, 16], [9, 3, 10, 9], [8, 25, 16, 16]],[8, 11, 10, 10, 16, 25] )
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_in_matrix.py",
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
