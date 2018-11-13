from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):
    cache = [[0 for _ in individual_play_scores] for _ in range(final_score + 1)]
    cache[0] = [1 for _ in individual_play_scores]

    for i in range(1, final_score + 1):
        if i >= individual_play_scores[0] and i % individual_play_scores[0] == 0:
            cache[i][0] = 1


    for j in range(1, len(individual_play_scores)):
        for i in range(1, final_score + 1):
            cache[i][j] = cache[i][j - 1]
            if i >= individual_play_scores[j]:
                cache[i][j] += cache[i - individual_play_scores[j]][j]
    return cache[final_score][len(individual_play_scores) - 1]
num_combinations_for_final_score(12, [2,3,7])
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
