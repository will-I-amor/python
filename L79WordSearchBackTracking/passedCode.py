class Solution:
    def helper(self,board,word,row,col):
        if (len(word)==0):return True
        if (row<0 or col<0 or row>= len(board) or col>=len(board[0]) or board[row][col]!=word[0]):return False
        temp = board[row][col] 
        board[row][col]="#"
        #注意这里一定是or
        if self.helper(board,word[1:],row+1,col) or self.helper(board,word[1:],row-1,col) or self.helper(board,word[1:],row,col+1) or self.helper(board,word[1:],row,col-1):
            return True
        else:
            board[row][col] = temp
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
