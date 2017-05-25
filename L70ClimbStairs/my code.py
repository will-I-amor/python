class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [1,2]
        if n<=2:
            return nums[n-1]
        else:
            for i in range(2,n):
                temp = nums[i-2]+nums[i-1]
                nums.append(temp)
            return nums[n-1]
