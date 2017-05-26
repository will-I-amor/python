# 自己写的非常长的code。。回头改进一下
class Solution(object):
    def addBinary(self, a1, b1):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a1)
        b = int(b1)
        c = []
        jinwei = 0
        if (a==0 and b==0):
            return "0"
        else:
            while (a>0 or b>0):
                if (a==0):
                    yuB = int(b%10)
                    b = int(b/10)
                    temp = yuB + jinwei
                    if (temp>=2):
                        jinwei = 1
                        liuwei = temp - 2
                        c.insert(0,liuwei)
                    else:
                        jinwei = 0
                        c.insert(0,temp)
                elif (b==0):
                    yuA = int(a%10)
                    a = int(a/10)
                    temp = yuA + jinwei
                    if (temp>=2):
                        jinwei = 1
                        liuwei = temp-2
                        c.insert(0,liuwei)
                    else:
                        jinwei = 0
                        c.insert(0,temp)
                else:
                    yuA = int(a%10)
                    yuB = int(b%10)
                    a = int(a/10)
                    b = int(b/10)
                    temp = yuA + yuB + jinwei
                    if (temp>=2):
                        liuwei = temp-2
                        jinwei = 1
                        c.insert(0,liuwei)
                    else:
                        jinwei = 0
                        liuwei = temp
                        c.insert(0,liuwei)
            if (jinwei ==1):
                c.insert(0,jinwei)
                convertTo = [str(item) for item in c]
                str1 = ''.join(convertTo)
                return str1
            else:
                cTo = [str(item) for item in c]
                str2 = ''.join(cTo)
                return str2
