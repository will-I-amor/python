aDic = {'A':['B','F'],'B':['C','I','G'],'C':['B','I','D'],'D':['C','I','G','H','E'],'E':['D','H','F'],'F':['A','G','E'],'G':['B','F'],'H':['G','E','D'],'I':['B','C','D']}
print len(aDic)
def dfs(aDic,a,visited):
    visited[ord(a)-65] = True
    #mark as visited
    print a#output to console
    #assume a is 'A'
    #then aDic[a] = ['B','F']
    for i in aDic[a]:
        if visited[ord(i)-65] == False:
            dfs(aDic,i,visited)
def dfs_rec(aDic,a):
    n = len(aDic)
    visited = [x for x in range(n)]
    for i in range(n):
        visited[i] = False
    #I've initialized all the items in visited as FALSE
    dfs(aDic,a,visited)
dfs_rec(aDic,'A')
