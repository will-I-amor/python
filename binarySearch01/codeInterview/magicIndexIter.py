nums1 = [-40,-20,-1,1,2,3,5,7,9,12,13]
nums = [-1,0,2,5,7,9]
def magic(nums):
    start = 0
    end = len(nums)-1
    flag = -1
    while start<=end:
        mid = int((start+end)/2)
        if nums[mid]==mid:
            flag = mid
            return flag
        elif nums[mid]<mid:
            start=mid+1
        else:
            end = mid-1
    return flag
print (magic(nums1))
