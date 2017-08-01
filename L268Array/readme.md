    Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

    For example,
    Given nums = [0, 1, 3] return 2.

这道题tricky的地方在于input的变化多端。首先input的array不是sorted的，比如可能的input有:

    [0] -> 1
    [1] -> 0
    [2,0] -> 1
    [1,2] -> 0
    [2,3,0] -> 1
