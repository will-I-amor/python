    Given an index k, return the kth row of the Pascal's triangle.

    For example, given k = 3,
    Return [1,3,3,1].

    Note:
    Could you optimize your algorithm to use only O(k) extra space?
    
###### 因为题目要求用尽量少的空间，所以不能像上一道题一样存一个matrix，不能“下一行是上一行的一个XX操作”
###### 所以搞一个while loop来控制一行一行地算list，用for loop算出每行的list
###### 每行的arr[i]是用上一行的arr[i-1]+arr[i]算出来的。画个图就知道，看每行“下标”之间的加减关系
