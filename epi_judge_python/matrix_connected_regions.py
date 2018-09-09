from test_framework import generic_test
from collections import namedtuple, deque

Point = namedtuple("Point", ["x", "y"])

def flip_color(x, y, image):
    to_flip = DFS(x,y, image)
    for pt in to_flip:
        image[pt.y][pt.x] = 1 if image[pt.y][pt.x]  == 0 else 0

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


    def helper(curr):

        steps = [Point( curr.x - 1, curr.y),
                 Point(curr.x + 1, curr.y),
                 Point(curr.x, curr.y - 1),
                 Point(curr.x, curr.y + 1)]

        for step in steps:
            if step not in explored and is_valid(curr, step, image):
                explored.add(step)
                helper(step)


    explored = {Point(y,x)}
    helper(Point(y, x))

    return explored



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
