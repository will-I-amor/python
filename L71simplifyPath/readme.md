##### .join(foo)的用法， foo.split('/')的用法

##### python里用list实现stack，pop()即pop出最后item，append(i)从最后放进list

###### split后会把string里的'/'，以''空char的形式替代
    path = "/home//foo/"
    print (path.split('/'))
    # 输出['', 'home', '', 'foo', '']
