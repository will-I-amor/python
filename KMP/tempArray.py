#Compute temporary array to maintain size of suffix which is same as prefix
#Time/space complexity is O(size of pattern)
def computeTemporaryArray(pattern):
    lpattern = len(pattern)
    lps = []
    for j in range(lpattern):
        lps.append(0)
    index = 0
    i = 1
    while (i<lpattern):
        if pattern[i]==pattern[index]:
            lps[i] = index+1
            index+=1
            i+=1
        else:
            if index!=0:
                index = lps[index-1]
            else:
                lps[i]=0
                i+=1
    return lps
pattern = ['a','b','a','b','a','c','a']
lps = computeTemporaryArray(pattern)
print (lps)
