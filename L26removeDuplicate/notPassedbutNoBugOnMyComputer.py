nums = [1,1,2,3,4,4,4,4,4,4]
nums1 = [1,2,3,3]
nums2 = [1,2,2,3,4,4]
nums3 = [1,1,2]
def removeDup(nums):
    if len(nums)==0:
        return 0
    if len(nums)==1:
        return 1
    i = 0
    j = 1
    count = 1
    n = len(nums)
    while i<n and j<n:
        if nums[i]!=nums[j] and j-i>1:
            count+=1
            nums[i+1]=nums[j]
            i = i+1
            j+=1
        elif nums[i]!=nums[j] and j-i==1:
            count+=1
            i+=1
            j+=1
        else:
            j+=1
    print (nums)
    return count
print (removeDup(nums3))
