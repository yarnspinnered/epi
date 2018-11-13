from test_framework import generic_test
import heapq
from collections import deque
def minimum_path_weight(triangle):
    # TODO - you fill in here.
    if not triangle:
        return 0
    cache = [triangle[0][0]]

    for i in range(1, len(triangle)):
        new_cache = [0 for _ in range(i + 1)]
        for j in range(len(new_cache)):
            new_cache[j] = min(cache[j-a] for a in (0,1) if 0 <= j -a < len(cache))  \
                           + triangle[i][j]
        cache = new_cache

    return min(cache)

#DIJKSTRA. Doesnt work there are negative edges.
# def minimum_path_weight(triangle):
#     # TODO - you fill in here.
#     if not triangle:
#         return 0
#     cost = [[float('inf') for node in row] for row in triangle]
#     cost[0][0] = triangle[0][0]
#     explored = [[False for node in row] for row in triangle]
#     explored[0][0] = True
#     pq = [(triangle[0][0], (0,0))]
#
#
#     while pq:
#         curr_cost, curr_pos = heapq.heappop(pq)
#         for i,j in [(curr_pos[0] + 1, curr_pos[1]),(curr_pos[0] + 1, curr_pos[1] + 1)]:
#             if j <= i and i < len(triangle) and not explored[i][j]:
#                 cost[i][j] = min(cost[i][j], curr_cost + triangle[i][j])
#                 heapq.heappush(pq, (cost[i][j], (i,j)))
#         explored[curr_pos[0]][curr_pos[1]] = True
#
#     return min(cost[len(triangle) - 1])

minimum_path_weight([[2], [4, 4], [8, 5, 6], [4, 2, 6, 2], [1, 5, 2, 3, 4]])
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_weight_path_in_a_triangle.py",
                                       'minimum_weight_path_in_a_triangle.tsv',
                                       minimum_path_weight))
