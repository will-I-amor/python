#though slow, but accepted
#如果graph上一个item是0，就把相应的row和col上的数都设为0
G = [[0, 1, 2], [3, 4, 5], [6, 0, 8], [9, 10, 11]]
rowlist = [] #for storing row number
collist = [] #我把row和col分开存储
for row in range(len(G)):
    for col in range(len(G[row])):
        if G[row][col]==0:
            rowlist.append(row)
            collist.append(col)
print ("rowlist:",rowlist)
print ("collist:",collist)
while (rowlist!=[] and collist!=[]):
    temprow = rowlist.pop() #再一个个地把有0的row和col一个个pop出来，用来设其他数为0
    tempcol = collist.pop()
    for i in range(len(G[0])):
        G[temprow][i]=0
    for j in range(len(G)):
        G[j][tempcol]=0
print (G)
#只打败12%的人，非常慢的code，要优化
