def searchMatrix(self, matrix, target):
        """
        比如G= [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
        """
        if not matrix or not matrix[0]:
            return False
        row = len(matrix)
        col = len(matrix[0])
        start = 0
        end = (row*col)-1
        flag = False
        while (start<=end):
            mid = int((start+end)/2)
            num = matrix[int(mid/col)][int(mid%col)]
            if target<num:
                end = mid-1
            elif target>num: 
                start = mid+1
            else:
                flag = True
                return flag
        return flag
