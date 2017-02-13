class Solution(object):
    def binarySearch(self,nums,target):
        if (len(nums)==0):
            return -1
        else:
            start = 0
            end = len(nums)-1
            while (start<=end):
                mid = start + (end-start)/2
                if (target==nums[mid]):
                    return mid
                elif (target>nums[mid]):
                    start = mid + 1
                else:
                    end = mid - 1
            return -1
    def search(self, nums, target):
        n = len(nums)
        if (n==0):
            return -1
        else:
            rem = -1
            for i in range(n-1):
                if nums[i+1]<nums[i]:
                    rem = i
            print "rem: ",rem
            if (rem==-1):#if everything is sorted
                #print "1:",binarySearch(nums,target)
                return self.binarySearch(nums,target)
            else:
                if (target<=nums[rem] and target>=nums[0]):
                    aList1 = nums[0:rem+1]
                    if (len(aList1)==0):
                        print 2
                        return -1
                    else:
                        t = self.binarySearch(aList1,target)
                        print aList1
                        print 3
                        return t
                else:
                    aList2 = nums[rem+1:n]
                    print "aList2:",aList2
                    if(len(aList2)==0):
                        print 4
                        return -1
                    else:
                        s = self.binarySearch(aList2,target)
                        if (s==-1):
                            print 5
                            return s
                        else:
                            print 6
                            return rem+1+s