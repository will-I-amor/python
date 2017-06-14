def threepointers(a):
    cur = 0
    begin = 0
    end = len(a)-1
    while (cur<=end):
        if a[cur]==0:
            a[cur],a[begin]=a[begin],a[cur]
            cur+=1
            begin+=1
        elif a[cur]==1:
            cur+=1
        else:
            a[cur],a[end]=a[end],a[cur]
            end-=1
    return a
nums = [0,0,0]
b = []
a = [1,2,0,0,1,1,2,0]
nNum = threepointers(nums)
print (nNum)
