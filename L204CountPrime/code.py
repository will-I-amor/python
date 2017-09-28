class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n<3):return 0
        f = [1]*n
        f[0]=f[1]=0
        count = 0
        for i in range(2,int(math.sqrt(n))+1):#这里sqrt(n)后面要+1，不然index会有问题
            if (f[i]):
                for j in range(i*i,n,i):
                    f[j]=0
        for it in f:
            if(it==1):
                count+=1
        return count
