from test_framework import generic_test

# not done
def multiply(num1, num2):

    negative = False
    if (num1[0] < 0 and num2[0] > 0) or (num2[0] < 0 and num1[0] > 0):
        negative = True
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])

    res = [0 for x in range(len(num1) +len(num2))]

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            val = num1[i] * num2[j] + res[i + j + 1]
            res[i + j + 1] = val % 10
            res[i + j] += val // 10

    i = 0
    while i < len(res):
        if res[i] != 0:
            break
        i += 1
    res = res[i:]

    if not res:
        res = [0]
    if negative:
        res[0] = res[0] * - 1

    return res

# print(multiply([1,2], [1,9]))
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
