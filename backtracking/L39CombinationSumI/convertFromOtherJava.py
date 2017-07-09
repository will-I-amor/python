#this file can get passed as well
def combinationSumHelper(nums,target,index,results,curSeq):
    if target==0:
        results.append(curSeq)
    elif target>0:
        for i in range(index,len(nums)):
            if nums[i]<=target:
                #curSeq.append(nums[i])
                combinationSumHelper(nums,target-nums[i],i,results,curSeq+[nums[i]])
                #curSeq.pop()
                #in Java, you should pop the last item, BC line8&9,
                #we actually append the nums[i] to curSeq and pass it along in the recursion
def combinationSum(nums,target):
    results = []
    nums.sort()
    curSeq = []
    combinationSumHelper(nums,target,0,results,curSeq)
    return results
nums = [2, 3, 6, 7]
nums1 = [1,2]
c = combinationSum(nums1,4)
print (c)
