#这道题是一次可以爬1，2，3阶楼梯，是coding interview上的题
nums = [1,2,4]
def climbS(n,nums):
    if n<0:
        return 0
    elif n<=3:
        return nums[n-1]
    elif n<len(nums):
        return nums[n-1]
    else:
        temp = climbS(n-1,nums)+climbS(n-2,nums)+climbS(n-3,nums)
        nums.append(temp)
        #nums[n]=countWaysDP(n-1,nums)+countWaysDP(n-2,nums)+countWaysDP(n-3,nums)
        return nums[n-1]
climbS(5,nums)
print (nums)
#output   [1, 2, 4, 7, 13]



#之前的一个方法：
def countWays(n):
    if (n<0):
        return 0
    elif n==0:
        return 1
    else:
        return countWays(n-1)+countWays(n-2)+countWays(n-3)
nums = []
for i in range(5):
    temp = countWays(i)
    nums.append(temp)
    return countWays(n-1)+countWays(n-2)+countWays(n-3)
print (nums)
###output:  [1, 1, 2, 4, 7]
#A child is running up a staircase with n steps, and can hop either 1 step, 2 steps, or 3 steps at a time.
#We can approach this problem from the top down. On the very last hop, up to the nth step, the child could have done either a single, double, or 
#
        
