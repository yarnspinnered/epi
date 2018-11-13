from test_framework import generic_test
from collections import deque

def is_pattern_contained_in_grid(grid, S):
    def helper(i,j,c_offset):

        if c_offset == 0 or any( (i + a, j + b, c_offset - 1) in cache
                                   for a,b in [(0,1), (1,0), (-1,0), (0, -1)]
                                   if 0 <= i + a < len(grid)
                                    and 0 <= j + b < len(grid[0])):
            new_cache.add((i,j,c_offset))

    cache = set()
    new_cache = set()
    for c in range(len(S)):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if S[c] == grid[i][j]:
                    helper(i,j,c)
        cache.clear()
        cache.update(new_cache)
        new_cache.clear()

    return any(len(S) - 1 == c for i, j, c in cache)

# def is_pattern_contained_in_grid(grid, S):
#     def dfs(i, j, offset):
#         if offset == len(S):
#             return True
#         if (i,j,offset) in cache:
#             return False
#         if 0 <= i < len(grid) \
#             and 0 <= j < len(grid[i]) \
#             and grid[i][j] == S[offset] \
#             and any(dfs(i+a, j + b, offset + 1) for a,b in [(-1, 0), (1, 0), (0, -1), (0, 1)]):
#                 return True
#
#         cache.add((i,j, offset))
#         return False
#
#     cache = set()

    return any(dfs(i,j,0) for i in range(len(grid)) for j in range(len(grid[i])))
is_pattern_contained_in_grid([[8, 11, 10, 16], [9, 3, 10, 9], [8, 25, 16, 16]],[8, 11, 10, 10, 16, 25] )
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_in_matrix.py",
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
