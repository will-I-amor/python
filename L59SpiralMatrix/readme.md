    Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

    For example,
    Given n = 3,

    You should return the following matrix:
    [
     [ 1, 2, 3 ],
     [ 8, 9, 4 ],
     [ 7, 6, 5 ]
    ]
    
这道题用i来走，用l=k=0, last_col = n-1, last_row = n-1来控制走向。用i来在这些变量间循环
![](https://i.imgur.com/FdqcDvQ.jpg)
