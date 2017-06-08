比如G = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
],每个row都是升序排列，每行第一个都比上一行最后一数大。以binary search的方法找target在不在这个矩阵里

找mid数是(start+end)/2,之前在这里bug蛮久的。之前写的是mid = start+(end-start)/2

这道题binary search最容易的方法就是把这几个row都拼到1行上来search。
所以end就是(row*col)-1

然后找到mid之后，要算mid在matrix里是第几row第几col。就是matrix[mid/col][mid%col]
