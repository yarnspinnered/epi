import functools
from collections import Counter
import heapq
import collections

def compute_top_k_variance(students, scores, k):
    counts = {}
    for i in range(len(students)):
        if students[i] not in counts:
            counts[students[i]] = 1
        else:
            counts[students[i]] += 1
    print(Counter(students))
    all_scores = {}
    for key in counts:
        if counts[key] >= k:
            all_scores[key] = []

    for i in range(len(students)):
        if students[i] in all_scores:
            all_scores[students[i]].append(scores[i])
    print("asll_scores: ", all_scores)
    top_k_scores = {}
    for key in all_scores:
        sorted_scores = sorted(all_scores[key])
        top_k_scores[key] = []
        for i in range(k):
            top_k_scores[key].append(sorted_scores[len(sorted_scores) - 1 - i])

    result = {}
    for key in top_k_scores:
        total = 0
        for score in top_k_scores[key]:
            total += score
        mean = total / k
        variance = 0
        for score in top_k_scores[key]:
            variance = variance + (score - mean) **2
        result[key] = variance
    return result

def compute_top_k_variance2(students, scores, k):
    counts = Counter(students)
    all_scores = collections.defaultdict(list)
    for student, score in zip(students,scores):
        all_scores[student].append(score)

    top_k_scores = {
        student : heapq.nlargest(k, scores)
        for student, scores in all_scores.items() if counts[student] >= k
    }

    result = {
        student: functools.reduce(lambda z,x: z + (x - mean)**2, scores, 0)
        for student, scores, mean in (
        (student, scores, sum(scores)/k) for student,scores in top_k_scores.items()
    )
    }
    return result
print("old: ", compute_top_k_variance(["a","a","a","b","b"], [1,2,3,2,2], 3))
print("new: ", compute_top_k_variance2(["a","a","a","b","b"], [1,2,3,2,2], 3))