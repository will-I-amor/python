class Solution:
    def helper(self,board,word,row,col):
        if (len(word)==0):return True
        if (row<0 or col<0 or row>= len(board) or col>=len(board[0]) or board[row][col]!=word[0]):return False
        temp = board[row][col] 
        board[row][col]="#"#这里是表明，我们已经采用了现在的这个字母(当前row col上的这个字母)，我们以后就不能再用了，所以改成'#'
        #注意这里一定是or
        if self.helper(board,word[1:],row+1,col) or self.helper(board,word[1:],row-1,col) or self.helper(board,word[1:],row,col+1) or self.helper(board,word[1:],row,col-1):
            return True
        else:
            board[row][col] = temp
            #这里还要再改回来，就是我们要开始下一层recursion了，不能再用#号了。一般backtracking都会改一个东西，然后再给改回来
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board,word,i,j):
                    return True
        return False
