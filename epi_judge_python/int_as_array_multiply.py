from test_framework import generic_test

def multiply(num1, num2):

    sign = 1
    if (num1[0] < 0 and num2[0] > 0) or (num2[0] < 0 and num1[0] > 0):
        sign = -1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    res = [0 for _ in range(len(num1) + len(num2))]

    for i in reversed(range(len(num2))):
        for j in reversed(range(len(num1))):
            v = num2[i] * num1[j] + res[i + j + 1]
            res[i + j] += v //10
            res[i + j + 1] = v % 10

    res = res[next((i for i, x in enumerate(res) if x != 0), len(res)):] or [0]

    return [sign * res[0]] + res[1:]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
