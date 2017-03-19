def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        else:
            i = len(s)-1
            flag = True
            while (s[i]==' ' and i>=0):#i一定要大于等于0,否则out of index出界
                i-=1
            n = 0
            while (i>=0 and s[i]!=' '):
                n += 1
                i -= 1
            return n
