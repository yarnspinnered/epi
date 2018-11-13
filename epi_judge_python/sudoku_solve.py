import copy
import functools
import math
import itertools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from epi_judge_python_solutions.is_valid_sudoku import is_valid_sudoku
from collections import Counter
def solve_sudoku(partial_assignment):
    def valid_to_add(i, j, val, partial_assignment):
        # Check row constraints.
        if any(val == partial_assignment[k][j]
               for k in range(len(partial_assignment))):
            return False

        # Check column constraints.
        if val in partial_assignment[i]:
            return False

        # Check region constraints.
        region_size = int(math.sqrt(len(partial_assignment)))
        I = i // region_size
        J = j // region_size
        return not any(
            val == partial_assignment[region_size * I + a][region_size * J
                                                           + b]
            for a, b in itertools.product(range(region_size), repeat=2))

    def helper(offset):
        if offset == 81:
            if is_valid_sudoku(state):

                for i in range(9):
                    for j in range(9):

                        partial_assignment[i][j] = state[i][j]
                return True
            return False
        r,c = offset // 9, offset % 9
        if partial_assignment[r][c] != 0:
            return helper(offset + 1)
        for x in range(1, 10):
            if valid_to_add(r, c, x, state):
                state[r][c] = x
                if helper(offset + 1):
                    return True
            state[r][c] = 0
        return False

    state = [[x for x in r] for r in partial_assignment]
    solvable = helper(0)

    return


def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))

    for i in range(len(solved)):
        assert_unique_seq(solved[i])
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sudoku_solve.py", 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
