#用iteration来binary search
def magicFast(nums,start,end):
    if (end<start or start<0 or end>=len(nums)):
        return -1
    mid = int((start+end)/2)
    if nums[mid]==mid:
        print ("mid")
        return mid
    elif nums[mid]>mid:
        return magicFast(nums,start,mid-1)
    else:
        return magicFast(nums,mid+1,end)
nums1 = [-40,-20,-1,1,2,3,5,7,9,12,13]
print (magicFast(nums1,0,len(nums1)-1))
