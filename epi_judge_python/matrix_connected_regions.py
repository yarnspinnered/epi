from test_framework import generic_test
from collections import namedtuple, deque

Point = namedtuple("Point", ["x", "y"])

def flip_color(x, y, image):
    DFS(x,y, image)
    return

def BFS(i,j, image):
    q = deque()
    explored = {Point(j,i)}
    q.append(Point(j,i))

    while q:
        curr = q.pop()
        steps = [Point(curr.x - 1, curr.y),
                 Point(curr.x + 1, curr.y),
                 Point(curr.x, curr.y - 1),
                 Point(curr.x, curr.y + 1)]

        for step in steps:
            if step not in explored and is_valid(curr, step, image):
                q.appendleft(step)
                explored.add(step)

    return explored

def DFS(x,y, image):
    if not image:
        return set()

    base_col = image[x][y]
    other_col = 1 ^ base_col
    dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    def helper(x,y):
        if image[x][y] == other_col:
            return
        image[x][y] = other_col
        for dx,dy in dirs:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(image) and \
                    0 <= new_y < len(image[new_x]):
                # image[new_x][new_y] = other_col
                helper(new_x, new_y)



    helper(x,y)

    return



def is_valid(src, dst, image):
    height = len(image)
    width = len(image[0])
    return dst.x >= 0 and dst.x < width and\
           dst.y >= 0 and dst.y < height and\
           image[dst.y][dst.x] == image[src.y][src.x]

def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
