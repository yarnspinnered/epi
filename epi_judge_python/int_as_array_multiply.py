from test_framework import generic_test

# not done
def multiply(num1, num2):
    def multiply_single_digit(larger, smaller):
        res = []
        neg_cnt = 0
        if smaller[0] < 0:
            neg_cnt += 1
            smaller[0] *= -1
        if larger[0] < 0:
            neg_cnt += 1
            larger[0] *= -1
        for j in range(-1, -len(larger) - 1, -1):
            v1 = smaller
            v2 = larger[j]
            if j * -1 > len(res):
                res.insert(0, 0)
            pdt = v1 * v2 + res[j]
            res[j] = pdt % 10
            if pdt // 10 > 0 :
                if 1 - j > len(res):
                    res.insert(pdt // 10, 0)
                else:
                    res[j - 1] += pdt // 10
        if neg_cnt == 1:
            res[0] *= -1
        return res
    def add_two_arrays(num1, num2):
        shorter = num2
        longer = num1
        if len(num1) <= len(num2):
            shorter = num1
            longer = num2
        for i in range(-1, -1 * len(shorter), -1):
            new_sum = shorter[i] + longer[i]
            longer[i] = new_sum % 10
            if
            longer[i - 1] = new_sum // 10

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
