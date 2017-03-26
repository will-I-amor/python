#webpage:http://www.geeksforgeeks.org/replace-occurrences-string-ab-c-without-using-extra-space/
import pdb
def replace(alist):
    n = len(alist)
    i = 0
    j = 0
    count = 0
    while (j<n-1):
        #pdb.set_trace()
        if (alist[j]=='A' and alist[j+1]=='B'):
            alist[i] = 'C'
            j+=2
            i+=1
            count+=1
        else:
            alist[i]=alist[j]
            j+=1
            i+=1
    if (j==n-1):
        if alist[j-1]=='A' and alist[j]=='B':
            alist[i]='C'
        else:
            alist[i]=alist[j]
    newlist = []
    #newlist = alist[:i]
    newlist = alist[:n-count]#no need for n-count+1,bc n is 1 more than n-1
    print newlist
    
a = "hABwABl"
a1 = "helloWorldAB"
a2 = "ABAB"
a3 = ""
alist = list(a3)
replace(alist)
