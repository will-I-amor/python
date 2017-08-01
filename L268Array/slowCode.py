 def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if(len(nums))==1:
            if nums[0]==1:
                return 0
            elif nums[0]==0:
                return 1
            else:
                return nums[0]+1
        i = 0
        j = 1
        n = len(nums)
        temp = 0
        while i<=n-2 and j<=n-1:
            if nums[j]-nums[i]==1:
                i+=1
                j+=1
            else:
                temp = nums[i]+1
                return temp
                break
        if nums[0]!=0:
            return 0
        else:
            return nums[n-1]+1
