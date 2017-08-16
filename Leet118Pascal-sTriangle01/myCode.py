def getArray(n,matrix):
    newArray = [1,1]
    for i in range(1,n):#n starts from 3
        temp = matrix[n-1][i-1]+matrix[n-1][i]
        newArray.insert(1,temp)
    return newArray
#用getArray计算出每行的array


def drive(row):
    if row==1: return [[1]]
    elif row==2: return [[1],[1,1]]
    elif row==0: return []
    else:
        matrix = [[1],[1,1]]
        for i in range(2,row):
            tempRow = getArray(i,matrix)
            matrix.append(tempRow)
            //把每行的array加进matrix
        return matrix
matrix = drive(7)
print (matrix)
