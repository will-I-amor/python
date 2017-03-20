x = [21, 40, 9, 38, 34, 42]
def merge(a,b):
    i,j = 0,0
    result = []
    while (i<len(a) and j<len(b)):# bugged if "and" change to "or"
        if a[i]<b[j]:
            result.append(a[i])
            i+=1
        else:
            result.append(b[j])
            j+=1
    result+=a[i:]
    result+=b[j:]
    return result
def mergeSort(x):
    if len(x)==1:
        return x
    else:
        n = len(x)
        a = mergeSort(x[:n/2])
        b = mergeSort(x[n/2:])
        return merge(a,b)

result = mergeSort(x)
print result
