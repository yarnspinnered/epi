from test_framework import generic_test

# not done
def multiply(num1, num2):
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])

    res = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            res[i+j+1] += (num1[i] * num2[j]) % 10
            res[i+j] += (num1[i] * num2[j]) // 10
    i = 0
    while res[0] == 0 and i < len(res):
        i += 1
    res = res[i:]

    res[0] *= sign
    return res

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
