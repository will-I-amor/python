G = [[0 for xx in range(n)]for yy in range(n)]
l = k = i = 0
l_col = l_row = n-1
count = 1
while(l<=l_col and k<=l_row):
    for i in range(l,l_col+1):
        G[k][i]=count
        if(k==1 and i==2):
            print("1")
        count+=1
    k+=1
    for i in range(k,l_row+1):
        #print("count",count)
        G[i][l_col]=count#之前这里出了bug，col和row写反了
        #print("G[l_col][i]:",G[l_col][i],"l_col:",l_col,"i:",i)
        count+=1
    l_col-=1
    if(l<=l_col):
        for i in range(l_col,l-1,-1):
            G[l_row][i]=count
            if(l_row==1 and i==2):
                print("2")
            count+=1
        l_row-=1
    if(k<=l_row):
        for i in range(l_row,k-1,-1):
            G[i][l]=count
            if(i==1 and l==2):
                print("3")
            count+=1
        l+=1
print(G)
