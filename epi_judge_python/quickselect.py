import random
def quickselect(A, k, l , r):
    def partition(l,r,p):
        v = A[p]
        A[r], A[p] = A[p], A[r]
        clean = l
        for i in range(l,r):
            if A[i] <= v:
                A[clean], A[i] = A[i], A[clean]
                clean += 1
        A[clean], A[r] = A[r], A[clean]
        return clean

    p = random.randint(l,r)
    p = partition(l,r, p)
    # print(p, A[p], all(x <= A[p] for x in A[:p + 1]))
    if p == k:
        return A[p]
    elif p < k:
        return quickselect(A,k,p + 1, r)
    else:
        return quickselect(A,k,l, p - 1)

N = 100
arr = list(x for x in range(N))
random.shuffle(arr)
print(quickselect(arr, 23, 0, N - 1))