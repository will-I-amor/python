'''given: ["eat", "tea", "tan", "ate", "nat", "bat"]

Return:
[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]'''

a = ["eat", "tea", "tan", "ate", "nat", "bat"]
def groupAnagrams(strs):
    dic = {}
    for i in a:
        temp = "".join(sorted(i))
        #i is like "eat,
        #after sorted(i), i will be "e","a","t"
        #use .join(),temp would be like "aet"
        #so we get rid of the ","
        if temp in dic:
            dic.get(temp).append(i)
            #dic[temp].append(i) is also right
            #dict.get() means, even thou there is no key like temp in dict
            #dict would creat a new key for temp
        else:
            dic[temp]=[i]#make i a list!!! so that .append() could be used
    return dic.values()
groupAnagrams(a)
