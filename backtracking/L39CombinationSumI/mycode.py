nums = [2, 3, 6, 7]
def helper(nums,i,target,sol,G):
    if(target==0):
        G.append(sol)
    if target>0:
        for j in range(i,len(nums)):
            if j>i and nums[j]==nums[j-1]:
                continue
            if nums[j]<=target:
                #sol.append(nums[j])
                helper(nums,j,target-nums[j],sol+[nums[j]],G)
                #NOTICE,we passed the sol+[nums[j]], in which we didn't CHANGE the sol list
                #the A+[b],passed to a function, didnt change A itself
                #把helper(nums[j:],target-nums[j])这行，里的nums[j:]改成nums才能Accepted
                #不知道为什么？？？？？？？
            if nums[j]>target:
                break
def combinationSum(nums,target):
    sol = []
    G = []
    nums.sort()
    helper(nums,0,target,sol,G)
    #print (G)
    return G
def main():
    nums = [2, 3, 6, 7]
    nums1 = [1,2]
    result = combinationSum(nums1,4)
    print (result)
if __name__ == "__main__":
    main()
