class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxi = max(nums)
        n = len(nums)
        if n == maxi+1:
            return maxi + 1
        ans = [0] * (n+1)
        for i in range(n):
            ans[nums[i]] = 1
        for i in range(len(ans)):
            if ans[i] == 0:
                return i  