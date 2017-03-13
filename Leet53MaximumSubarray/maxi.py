class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #I originally assign curMax with '0', but didn't work out, because
        #if don't assign the minInt to curMax,then when nums = [-1],only 1 int, then 0 would be the largest sum
        curMax = -9223372036854775807
        imax = -9223372036854775807
        for i in nums:
            if curMax<0:
                curMax = i
            else:
                curMax+=i
            if imax<curMax:
                imax = curMax
        return imax
