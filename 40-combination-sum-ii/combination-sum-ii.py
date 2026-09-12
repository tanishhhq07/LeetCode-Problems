class Solution(object):
    def combinationSum2(self, candidates, target):
        ans = []
        arr = []
        k = candidates
        n = len(k)
        k.sort()
        
        def backtrack(start,a):
            if a == target:
                ans.append(arr[:])
                return

            for i in range(start, n):
                if i > start and k[i] == k[i - 1]:
                    continue

                if a + k[i] > target:
                    break

                arr.append(k[i])
                backtrack(i + 1, a + k[i])
                arr.pop()
        backtrack(0,0)
        return ans