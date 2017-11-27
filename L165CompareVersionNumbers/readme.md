    比较版本号。这里2.5不是数字，而是版本号，也就是有可能会有19.03.08.5.66.7这种数字出现
    
    所以用split()函数，把'.'分出来。这题要考虑多种情况，比如01 vs 1  比如19.03.1和19.03.1.0.0.0是一样的
    
    Compare two version numbers version1 and version2.
    If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
    
    如果version1>version2返回1，反之返回-1，若相等，返回0
    
    You may assume that the version strings are non-empty and contain only digits and the . character.
    The . character does not represent a decimal point and is used to separate number sequences.
    For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

    Here is an example of version numbers ordering:

    0.1 < 1.1 < 1.2 < 13.37
