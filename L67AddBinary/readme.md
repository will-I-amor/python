##### 这道题是两个bianry数相加。比如a = "11", b = "1"
##### 输入的两个参数都是string类型
##### 我的思路是先把a1,b1变成int，然后一位位除，从个位开始，a和b相加
##### while loop里是考虑3种情况：
###### 1) a和b位数一样，即除着除着a和b是同步进行的
###### 2) a位数少于b的情况
###### 3) b位数少于a的情况
