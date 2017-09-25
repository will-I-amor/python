def search(nums,target):
    l = 0
    r = len(nums)-1
    while (l<=r):
        mid = (l+r)//2
        if(nums[mid]==target):
            return True
        while (l<mid and nums[l]==nums[mid]):
        #比如有个数组[5,0,1,2,5,5,5,5,5],这个nums[l]就等于nums[m]，就一直挪l
        #这也是duplicate和非duplicate数组的区别
            l+=1
        if (nums[l]<=nums[mid]):
            if (nums[l]<=target<=nums[mid]):
                r = mid-1
            else:
                l = mid + 1
        else:
            if(nums[mid]<=target<=nums[r]):
                l = mid + 1
            else:
                r = mid - 1
    return False
nums = [4,5,5,6,0,1,2]
flag = search(nums,5)
print (flag)
