//直接暴力解法，用split把'.'分出来，分出来变成["digitString1","digitString2"...]
//然后iterate数组，把string变成int，然后从前往后，比较每个int大小
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = []
        v2 = []
        v1 = version1.split('.')
        v2 = version2.split('.')
        digit1 = []
        digit2 = []
        for i in v1:
            digit1.append(int(i))
        for i in v2:
            digit2.append(int(i))
        n1 = len(digit1)
        n2 = len(digit2)
        if n1>n2://如果2个数组，个数不同的情况
            for i in range(n2):
                if digit1[i]>digit2[i]:
                    return 1
                elif digit1[i]==digit2[i]:
                    continue
                else:
                    return -1
            for j in range(n2,n1)://如果2个数组为[19,8,3,0,0],[19,8,3]就应该返回0(2数组相等)
                if digit1[j]!=0:
                    return 1//如果是[19,8,3,0,1]和[19,8,3]那还是n1大
            return 0
        elif n1<n2:
            for i in range(n1):
                if digit1[i]>digit2[i]:
                    return 1
                elif digit1[i]==digit2[i]:
                    continue
                else:
                    return -1
            for j in range(n1,n2)://和30行一样的思路，只不过这里是n1<n2
                if digit2[j]!=0:
                    return -1
            return 0//全部相等，就return 0
        else:
            for i in range(n1):
                if digit1[i]>digit2[i]:
                    return 1
                elif digit1[i]==digit2[i]:
                    continue
                else:
                    return -1
            return 0
