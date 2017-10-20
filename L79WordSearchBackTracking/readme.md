###### Given a 2D board and a word, find if the word exists in the grid.

###### The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

###### For example,
###### Given board =

    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
  
###### word = "ABCCED", -> returns true,
###### word = "SEE", -> returns true,
###### word = "ABCB", -> returns false.

之前报错list index越界，后来发现是board[row][col]里的row和col写反了。。

后来又开始报结果错误，就是本应是True的算成False。


原因是 helper函数里的return出现了问题，

    一定要 if ... or ..成立. or..成立. or.成立..这样，再return True。不能一个一个地return
