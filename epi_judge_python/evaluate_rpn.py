from test_framework import generic_test
import string
from operator import add, mul, floordiv, sub

def evaluate(expression):
    operators = {"+":add, "*":mul, "/":floordiv, "-":sub}
    expr_list = expression.split(",")

    s = []

    for exp in expr_list:
        if not exp in operators:
            s.append(exp)
        else:
            b,a = int(s.pop()), int(s.pop())
            s.append(operators[exp](a,b))

    return int(s[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))


