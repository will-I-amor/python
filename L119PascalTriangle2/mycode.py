import pdb
def getRow(rowIndex):
    if rowIndex == 0: return [1]
    if rowIndex == 1: return [1,1]
    else:
        arr = [1,1]
        alist = [1,1]
        j = 2
        while (j<=rowIndex):
            #pdb.set_trace()
            for i in range(1,j):#要注意i的range是1到j，而非1到rowIndex
                temp = arr[i-1]+arr[i]
                alist.insert(1,temp)
                #这里insert是一个一个往后串的，但是由于我们insert的数都是对称的，比如2，33，464
                #所以可以使用insert
            arr = alist
            alist = [1,1]
            j+=1
        return arr
myvec = getRow(4)
print (myvec)
