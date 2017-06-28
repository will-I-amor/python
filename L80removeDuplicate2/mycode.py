'''given SORTED array [1,1,1,2,2,3]
   return INT 5, [1,1,2,2,3]
   allow Two duplicates
   
   Similar question, compare it with Leetcode 26
'''

def removeDup(nums):
    n = len(nums)
    if n==0 or n==1:
        return n
    else:
        i = 0
        j = 1
        count = 1
        first = 0
        while i<n and j<n:
            if nums[i]==nums[j]:
                count+=1
                if count>2:
                    j+=1
                    first+=1
                    #print ("when i:",i,"  j is:",j,"  first is:",first)
                elif count==2:
                    nums[i+1]=nums[j]
                    i+=1
                    j+=1
                else:
                    nums[i]=nums[j]
                    i+=1
                    j+=1
            else: #!=
                if j-i>=2:
                    count = 1
                    nums[i+1]=nums[j]
                    i+=1
                    j+=1
                else:
                    i+=1
                    j+=1
                    count=1
        print (nums)
        #print ("outside i",i)
        #print ("outside j",j)
        return i+1
        
nums = [1,1,1,2,2,3]
nums1 = [1,2,2,2,2,3,3,4,4,4,5]
nums2 = [1,1,1,2,2,2,3]
nums3 = [0]
nums4 = [2,2,3,3]
nums5 = [1,1,2,2]
removeDup(nums5)
