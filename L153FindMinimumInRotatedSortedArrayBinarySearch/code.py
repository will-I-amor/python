class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return None
        start = 0
        end = len(nums)-1
        target = nums[-1]
        while (start+1<end):
            mid = int(start+(end-start)/2)
            if nums[mid]<=target:
                end = mid
            else:
                start = mid
        return min(nums[start],nums[end])
