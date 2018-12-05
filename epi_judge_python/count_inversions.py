from test_framework import generic_test


def count_inversions(A):
    count = 0
    def merge(L, R):
        nonlocal count
        l, r = 0, 0
        merged_arr = []
        for r in range(0, len(R)):
            while l < len(L) and L[l] <= R[r]:
                merged_arr.append(L[l])
                l += 1
            count += len(L) - l
            merged_arr.append(R[r])
        merged_arr += L[l:]

        return merged_arr

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        else:
            m = len(arr) // 2
            L,R = merge_sort(arr[:m]), merge_sort(arr[m:])
            sorted_arr = merge(L,R)
        return sorted_arr

    merge_sort(A)
    return count


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "count_inversions.py", 'count_inversions.tsv', count_inversions))
