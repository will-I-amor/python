#input is string, we use strToList, convert string to digit list
def strToList(str1):#take a "string",return [1,2,3,4]
    num1 = []
    for i in str1:
        temp = ord(i)-ord('0')
        num1.append(temp)
    return num1

#from the num2's end digit, we multiply the digit with num1
#note that the result is a graph,like: [],[0],[0,0],[0,0,0]
def multi(num1,digit,result):#num1 is a list; result is [] or [0,0,0,0,0]
    n = len(num1)
    jinwei = 0
    for i in range(n-1,0,-1):
        mysum = (digit*num1[i])+jinwei
        result.insert(0,mysum%10)
        jinwei = mysum/10
    #when i is 0
    mysum = digit*num1[0]+jinwei
    result.insert(0,mysum%10)
    jinwei = mysum/10
    if(jinwei!=0):
        result.insert(0,jinwei)
    return result
#take the multiply result(a graph),then add them all together
def addNum(mygraph):#takes a graph,return a list
    umax = 0
    for i in mygraph:
        if (len(i))>umax:
            umax = len(i)
    for i in mygraph:
        if (len(i))<umax:
            cha = umax - len(i)
            for j in range(cha):#bu qi 0
                i.insert(0,0)
    #now the longest length in graph is umax
    #made the lists all have same length like:
    #[[0, 1, 3, 6, 8], [0, 9, 1, 2, 0], [4, 5, 6, 0, 0]]
    result = []
    yushu = 0
    for j in range(umax-1,-1,-1):
        mysum = 0
        for i in range(len(mygraph)):
            mysum = mysum + mygraph[i][j]
        mysum = mysum + yushu
        result.insert(0,mysum%10)
        yushu = mysum/10
    while (yushu>0):
        result.insert(0,yushu%10)
        yushu = yushu/10
    return result
#这个multiply是主程序
def multiply(num1,num2):#num1,2 is string
    if (len(num1)==0 or len(num2)==0):
        return None
    elif (num1=='0' or num2=='0'):
        return '0'
    else:
        numa = strToList(num1)
        numb = strToList(num2)
        #build [],[0,0]
        mygraph = []
        for i in range(len(numb)):
            newl = []
            for j in range(i):
                newl.append(0)
            mygraph.append(newl)
        for x in range(len(numb)):
            mygraph[x] = multi(numa,numb[len(numb)-1-x],mygraph[x])
        #mygraph have been filled with numbers
        result = []
        result = addNum(mygraph)
        for xx in range(len(result)):
            temp = result[xx]+ord('0')
            result[xx] = str(unichr(temp))
        a = ''.join(result)
        print a
        return a
        #???corner case, num1 is 0
        #???return type should be string

num1 = "0"
num2 = "456"
multiply(num1,num2)
