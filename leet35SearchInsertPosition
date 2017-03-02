class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while (left<=right):
            mid = (right+left)/2
            if (nums[mid]<target):
                left = mid + 1
            else:
                right = mid - 1
        return left
