from test_framework import generic_test
from collections import namedtuple

Coordinate = namedtuple("Coordinate", ["row", "col"])

def fill_surrounded_regions(board):
    def DFS(start, board, explored):
        def helper(pos):
            steps = [Coordinate(pos.row - 1, pos.col),
                     Coordinate(pos.row + 1, pos.col),
                     Coordinate(pos.row, pos.col + 1),
                     Coordinate(pos.row, pos.col - 1)
                     ]
            for step in steps:
                if step not in explored and check_valid(step, board):
                    explored.add(step)
                    helper(step)

        if not check_valid(start, board) or start in explored:
            return
        explored.add(start)
        helper(start)

    if not board:
        return

    explored = set()

    for i in range(len(board)):
        for j in range(len(board[0])):
            if i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1:
                if i == 7 and j == 9:
                    print("asdasd")
                DFS(Coordinate(i,j), board, explored)


    for i in range(len(board)):
        for j in range(len(board[0])):
            if Coordinate(i,j) not in explored:
                board[i][j] = 'B'

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
