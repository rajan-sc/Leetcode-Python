class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pos = -1
        for i in range(n):
            if nums[i] == 0:
                pos = i
                break
        if pos == -1:
            return nums
        for i in range(pos+1,n):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        

