#这道题给一个[2,3,6,7]让找加起来等于7的所有组合，target为7
#用combination的方法来做。
def combinationSum(candidates,target):
    G = []#这里不能是G[[]],否则结果会多一个[]空array。一个个array往[]里加就行
    candidates.sort()
    dfs(G,candidates,target,0,[])
    return G;
def dfs(G,candidates,target,s,ans):
    if target==0: 
        G.append(ans[:])#这里一定要ans[:],如果只写ans[]的话，传进去的是空集
        #ans[:]和ans的区别就像是c++里的&引用，ans[:]传进去的是引用
        return #这里不能写break，否则报错
    for i in range(s,len(candidates)):
        if(candidates[i]>target):
            return
        ans.append(candidates[i])
        dfs(G,candidates,target-candidates[i],i,ans)#因为允许重复，所以下一层还是从i开始，而非i+1
        ans.pop()#回到原来那层，把candidates[i] pop出来
nums = [2,3,6,7]
target = 7
G = combinationSum(nums,target)
print(G)
