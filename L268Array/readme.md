    Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

    For example,
    Given nums = [0, 1, 3] return 2.

这道题tricky的地方在于input的变化多端。首先input的array不是sorted的，比如可能的input有:

    [0] -> 1
    [1] -> 0
    [2,0] -> 1
    [1,2] -> 0
    [2,3,0] -> 1

slowcode.py是用很慢的办法来写的，用了nums.sort()增加了时间开销

此题还可以用bit manipulation的方法来写，有一篇很好的文章，集中讲bit manipulation的应用

[bit manipulation的应用](http://blog.csdn.net/morewindows/article/details/7354571)

#### bit manipulation
- &: 都为1，才为1
- |：都为0，才为0
- ^: 相同为0，相异为1

这道题就是用到抑或,  **^**

任何数抑或0，结果为他自己。

> a ^ 0 = a

还有一个等式需要知道:

> a ^ b ^ b = a
    
自己抑或自己，结果为0。比如 b ^ b = 0

#### 回到题目

![用下标^nums[i]](http://i.imgur.com/n1rHoUn.png)

    nums1 = [2,3,0]
    nums = [7,5,4,6,2,1,0]
    x = 0
    for i in range(len(nums)):
        x = x^i^nums[i]
    x = x^len(nums)
    print (x)

其中 x = x^i^nums[i]就是在 0^0^2  ^1^3  ^2^0  ^3

自己抑或自己可以划去，就剩下0^1 = 1

x = x^len(nums),就是最后还有和3抑或一下
