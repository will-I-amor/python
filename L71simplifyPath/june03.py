'''Unix文件下的路径简化
   e.g. path = "/home/", => "/home"
        path = "/a/./b/../../c/", => "/c"
'''
path = "/a/./b/../../c/"
path2 = "/home/"
newPath = path.split("/")
print ("after split: ",newPath)  #after split:  ['', 'a', '.', 'b', '..', '..', 'c', '']
stack = []
for i in newPath:
    if i in ["","."]:
        pass
    elif i in [".."]:
        if stack!=[]:
            stack.pop()
    else:
        stack.append(i)
reStr = '/'.join(stack)
print ("after join: ", reStr)   #after join:  c
newreStr = '/'+reStr
print ("final result: ",newreStr)
