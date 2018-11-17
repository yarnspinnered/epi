from test_framework import generic_test
from collections import namedtuple, deque

Coordinate = namedtuple("Coordinate", ["row", "col"])

def fill_surrounded_regions(board):

    dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    explored = set()

    # assume starting point of BFS is white
    def BFS(i,j):
        if (i,j) in explored:
            return
        q = deque()
        explored.add((i,j))
        q.append((i,j))

        while q:
            x,y = q.pop()
            for dx,dy in dirs:
                if 0 <= x + dx < len(board) and 0 <= y + dy < len(board[x+dx]) and \
                        (x + dx, y + dy) not in explored and \
                        board[dx + x][y + dy] == "W":
                    explored.add((x + dx, y + dy))
                    q.appendleft((x + dx, y + dy))

    # Explore from sides
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "W" and \
                    (i == 0 or i == len(board) - 1 or j == 0 or j == len(board[i]) - 1):
                BFS(i,j)

    for i in range(len(board)):
        for j in range(len(board[i])):
            if (i,j) not in explored:
                board[i][j] = "B"
    return

def check_valid(pos, board):
    row_count = len(board)
    col_count = len(board[0])
    return pos.row >= 0 and pos.row < row_count and\
           pos.col >= 0 and pos.col < col_count and \
           board[pos.row][pos.col] == 'W'

def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_enclosed_regions.py",
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
