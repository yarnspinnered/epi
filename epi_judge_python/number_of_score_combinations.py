from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):
    sorted_scores = sorted(individual_play_scores)
    A = [[0]*len(sorted_scores) for x in range(1+final_score)]
    A[0] = [1] * len(sorted_scores)

    for j in range(len(sorted_scores)):
        curr_play = sorted_scores[j]
        for i in range(1, final_score + 1):
            if j > 0:
                A[i][j] += A[i][j - 1]
            if i >= curr_play:
                A[i][j] = A[i][j] + A[i - curr_play][j]

    return A[final_score][len(individual_play_scores) - 1]

num_combinations_for_final_score(12, [2,3,7])
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
