class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        n = len(nums)
        for i in range(n):
            x = x^i^nums[i]
        x = x^n
        return x
