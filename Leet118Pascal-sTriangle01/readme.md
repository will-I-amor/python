    Given numRows, generate the first numRows of Pascal's triangle.
    For example, given numRows = 5,
    Return
    
    [
        [1],
        [1,1],
        [1,2,1],
      
     [1,3,3,1],
     
    [1,4,6,4,1]
     ]

![](http://i.imgur.com/Tot6SHy.png)

每行的特点是，从第3行开始（如果从0开始算就是从第2行开始）， 下标1=上一行下标0+1   2=上一行1+2

第4行： 1=0+1，2=1+2,3=2+3

由此推出getArray的code

