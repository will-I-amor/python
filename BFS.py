def graph_BFS(G,s):
    inf = 1e8
    color = []
    Q = []
    count = 0
    n = len(G)
    for v in range(0,n):
        color.append(0)
    Q.append(s)
    count = count + 1
    color[s] = 1
    while(Q!=[]):
        temp = Q[0]
        print temp
        #下面是把color不为1的graph[count - 1]里的item放进Q
        if(count-1<n):
            for i in G[count-1]:
                if(color[i] == 0):
                    Q.append(i)
        Q.remove(temp)
        count = count + 1
        #放进Q里的item变颜色
        for v in Q:
            color[v] = 1
graph = [[1,2,3],[5],[],[4],[5],[]]
graph1 = [[1],[2,3,4],[3,4],[],[]]
graph2 = [[1,2],[3],[0,4,5],[],[2,5,7],[2,4,7,6],[5,7],[4,5,6]]
source = 0
graph_BFS(graph2,source)