G1 = [[25, 11], [22, 47], [48, 33], [44, 26], [21, 7], [7, 24]]
G2 = [[1,3],[2,6],[8,10],[15,18]]
G = [[1,3]]
G.sort()
#print G
newl = []
x = 0
while (x<len(G)):
    if len(newl)==0:
        if x<len(G)-1:
            if G[x][1]>=G[x+1][0]:
                temp = []
                temp.append(min(G[x][0],G[x+1][0]))
                temp.append(max(G[x][1],G[x+1][1]))
                newl.append(temp)
                x += 2
            else:
                newl.append(G[x])
                newl.append(G[x+1])
                x += 2
        else:
            newl.append(G[x])
    else:
        if newl[-1][1]>=G[x][0]:
            temp = []
            temp.append(min(newl[-1][0],G[x][0]))
            temp.append(max(newl[-1][1],G[x][1]))
            newl.remove(newl[-1])
            newl.append(temp)
            x += 1
        else:
            newl.append(G[x])
            x += 1
print newl
  
