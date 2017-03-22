#### othersMethod里一个lambda Sort比较有意思，对于class定义的intervals，用intervals.sort()无法sort他
#### 而且intervals也不是一个matrix
#### matrix可以用sort()来排序
### 如下图，没法sort
![](http://i1.piimg.com/567571/f8ad32e28c700113.png)

## wrongMethod的错误在于

- 1. 把intervals即G当成matrix

- 2. 冗余思考。情况分的太多，太多if，其实很多情况是重叠的。在sorted了的情况下，newl里面放了东西下，有2种情况；没放，有1种情况。就可以了
