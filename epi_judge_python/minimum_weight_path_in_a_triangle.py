from test_framework import generic_test
import heapq
from collections import deque
def minimum_path_weight(triangle):
    # TODO - you fill in here.
    if not triangle:
        return 0
    cache = [[float('inf') for node in row] for row in triangle]
    cache[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        for j in range(i + 1):
            candidates = []
            if j - 1 >= 0:
                candidates.append(cache[i-1][j-1])
            if j < i:
                candidates.append(cache[i-1][j])
            cache[i][j] = min(candidates) + triangle[i][j]

    return min(cache[len(triangle) - 1])

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
