from test_framework import generic_test
import string
from operator import add, mul, floordiv, sub

def evaluate(expression):
    operators = {'+': add, '-': lambda x,y : y - x, '/': lambda x,y : y//x, '*':mul}
    expr_list = expression.split(",")
    stack = []

    for expr in expr_list:
        if expr in operators:
            stack.append(operators[expr](stack.pop(), stack.pop()))
        else:
            stack.append(int(expr))

    return stack[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
