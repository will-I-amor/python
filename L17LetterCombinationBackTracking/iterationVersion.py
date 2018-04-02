class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = [""]
        dic = {"0":" ","1":"","2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        if len(digits)==0:
            return []
        if len(digits)==1:
            res = []
            for cha in dic[digits[0]]:
                res.append(cha)
            return res
        for digit in digits:
            newresult = []
            lst = dic[digit]
            for char in lst:
                for st in result:
                    newresult.append(st+char)
            result = newresult
        return result
