from test_framework import generic_test


def multiply(x, y):
    if x == 0 or y == 0:
        return 0
    def add(a,b):
        carryin, running_sum, k, temp_a, temp_b = 0, 0, 1, a, b

        while temp_a or temp_b:
            ak, bk = a & k, b & k
            running_sum |= ak ^ bk ^ carryin
            carryout = ak & bk | ak & carryin | b & carryin
            temp_a, temp_b, carryin, k = temp_a >> 1, temp_b >> 1, carryout << 1, k << 1
        return running_sum | carryin

    running_sum = 0
    while x:
        if x & 1:
            running_sum = add(running_sum, y)
        x, y = x >> 1, y << 1
    return running_sum
    # if y == 1:
    #     return x
    # elif y & 1:
    #     return add(multiply(x, y & (y -1)),x)
    # else:
    #     return multiply(x << 1, y >> 1)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("primitive_multiply.py",
                                       'primitive_multiply.tsv', multiply))
