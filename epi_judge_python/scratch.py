class Solution:
    def findMedianSortedArrays( A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        if len(A) > len(B):
            return findMedianSortedArrays(B, A)
        if len(A) == 0 and len(B) == 1:
            return B[0]
        # print(A,B)
        imin, imax = 0, len(A)
        n,m = len(A), len(B)
        while imin <= imax:
            i = (imin + imax) // 2
            j = (n - 2* i + m + 1)//2
            print(i, j)
            if i < n and A[i] < B[j - 1]:
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                imax = i - 1
            else:
                if i == 0:
                    left_max = B[j - 1]
                elif j == 0:
                    left_max = A[i - 1]
                else:
                    left_max = max(A[i - 1], B[j - 1])

                if i == n:
                    right_min = B[j]
                elif j == m:
                    right_min = A[i]
                else:
                    right_min = min(B[j], A[i])

                return (left_max + right_min) / 2 if (n + m) % 2 == 0 else left_max

    def isMatch(self, s, p):

        cache = {}
        def helper(i, j):
            print(s, p)
            if (i,j) in cache:
                return cache[(i,j)]
            if j == len(p):
                cache[(i, j)] = i == len(s)
                return cache[(i,j)]
            if i < len(s):
                first_match = s[i] == p[j] or p[j] == "."
            else:
                first_match = False

            if j < len(p) - 1 and p[j + 1] == "*":
                cache[(i, j)] = helper(i, j + 2) or (first_match and helper(i + 1, j))

            else:
                cache[(i, j)] = first_match and helper(i + 1, j + 1)
            return cache[(i,j)]

        return helper(0, 0 )

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        m = [x.lower() for x in ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')]

        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return [c for c in m[int(digits[0])]]

        tmp = self.letterCombinations(digits[1:])
        res = []

        for c in m[int(digits[0])]:
            for interm in tmp:
                res.append(c + interm)
        return res
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def helper(A, l, r):
            if len(A) == 2 * n:
                if l == r:
                    res.append(A)
                return
            if l < n:

                helper(A + "(", l + 1, r)
            if r < l:

                helper(A  + ")", l, r+ 1)


        helper("", 0, 0)
        return res

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        last = len(nums) - 1
        first_dec = -1

        for i in range(last, 0, -1):
            if nums[i - 1] < nums[i]:
                first_dec = i - 1
                break
        def swap(i,j):
            nums[i], nums[j] = nums[j], nums[i]
        def reverse(i):
            j = last
            while i < j:
                swap(i,j)
                i += 1
                j -= 1
        if first_dec == -1:
            reverse(0)
            return
        to_swap = len(nums)
        for i in range(first_dec + 1, len(nums)):
            if nums[i] > nums[first_dec]:
                to_swap = i

        swap(first_dec, to_swap)
        reverse(first_dec + 1)


s = Solution()
l = [1,2,3]
for i in range(7):
    s.nextPermutation(l)
    print(l)



