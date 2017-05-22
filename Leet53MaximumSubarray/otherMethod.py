def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum = 0
        maxSum = nums[0]#如果全负
        n = len(nums)
        for j in range(n):
            if curSum<0:#这种方法几乎跟上种一样，但是没上种设minimum值那么麻烦；如果curSum小于0，那么不论
                curSum = nums[j]#后面的数是什么，curSum必然小于curSum+nums[j]
            else:
                curSum += nums[j]
            maxSum = max(maxSum,curSum)
        return maxSum
