#加一而已，所以jinwei默认为1，留在原数位的书默认0
def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        jinwei = 0
        n = len(digits)
        if n==1:
            if digits[0]==9:
                digits = [1,0]
                return digits
            else:
                digits[0]+=1
                return digits
        temp = digits[n-1]+1
        if temp>9:
            jinwei = 1
            digits[n-1]=0
            for i in range(n-2,0,-1):#last is 1
                lsum = digits[i]+jinwei
                if lsum<10:
                    digits[i]=lsum
                    return digits
                else:
                    digits[i] = 0
                    jinwei = 1
            if jinwei==1:#add one digit
                if digits[0]+jinwei<10:
                    digits[0]+=jinwei
                    return digits
                else:
                    digits[0]=0
                    newdigits = [jinwei]+digits
                    return newdigits
        else:
            digits[n-1]=temp
            return digits
