from test_framework import generic_test


def step(curr):
    curr_alpha = curr[0]
    curr_cnt = 1
    j = 1
    res = ''
    while j < len(curr):
        if curr[j] == curr_alpha:
            curr_cnt += 1
        else:
            res += str(curr_cnt) + curr_alpha
            curr_alpha = curr[j]
            curr_cnt = 1
        j += 1
    res += str(curr_cnt) + curr_alpha

    return res

def look_and_say(n):
    if n == 0:
        return ''
    res = '1'
    for i in range(n - 1):
        res = step(res)


    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
