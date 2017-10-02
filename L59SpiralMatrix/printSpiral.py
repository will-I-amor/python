#把matrix螺旋的方式print出来
G = [['a','b','c','d','e'],['f','g','h','i','j'],['k','l','m','n','o'],['p','q','r','s','t']]
l = k = i = 0
l_col =5
l_row = 4
while(l<=l_col and k<=l_row):
    for i in range(l,l_col+1):
        print(G[k][i])
    k+=1
    for i in range(k,l_row+1):
        #pdb.set_trace()
        print(G[l_col][i])
    l_col-=1
    if(l<=l_col):
        for i in range(l_col,l-1,-1):
            print(G[l_row][i]);
        l_row-=1
    if(k<=l_row):
        for i in range(l_row,k-1,-1):
            print(G[i][l])
        l+=1
