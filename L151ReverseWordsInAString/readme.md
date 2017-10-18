    Given an input string, reverse the string word by word.

    For example,
    Given s = "the sky is blue",
    return "blue is sky the".
    要考虑到的因素有：前缀连续空格，后缀连续空格，和中间的连续空格(应变为1个空格)
    turnS = s[::-1]这是把s反转过来,变成eulb si yks eht
    
    if i!=" " and word!="" and turnS[j-1]==" ":
    这一句是判断，比如这种情况：(这是enumerate后print出来的)
    0 e
    1 u
    2 l
    3 b
    4  
    5 s
    6 i
    这个if判断的是当i是s时，s前头是空格，s本身不是空格，word里有东西，那么就把word+“ ”放进words里去
    
    elif i!=" ":
        word = i + word
    这句word = i + word要注意，这个是反着加的。因为turnS是完全反序的string了。我们在加回来的时候，要把当前指针指向的char，放到前一个去，插到前一个去
