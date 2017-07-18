题目是 A magic index in an array A[1...n-1] is defined to be an index such that A[i]=i. Given a SORTED array of distinct integers, write a method to find a magic index, if one exists, in array A


就是找出A[i]==i，即等同于他的下标的A[i]


比如nums = [-40,-20,-1,1,2,3,5,7,9,12,13] 应该return 7,即nums[7]==7


此题第一想法是遍历整个数组,brute force的方法挨个找

但是binary search可以更快捷


When we look at the middle element nums[5]=3, we know that the magic index must be on the right side, since nums[mid]<mid

如图所示，蓝线是下标的轨迹，橙线是可能的Nums[i]的轨迹

![Imgur](http://i.imgur.com/24WUx97.png)
