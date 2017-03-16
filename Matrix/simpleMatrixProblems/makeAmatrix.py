def makeaGraph(row,col):
    G = []
    count = 0
    for i in range(row):
        kong = []
        for j in range(col):
            kong.append(j+1+count)
        count+=col
        G.append(kong)
    return G
G = makeaGraph(3,3)
print G
