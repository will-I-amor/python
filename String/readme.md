#### 之前想的方法非常麻烦，从前往后遍历，遇到' '空格就记录下他的index,然后再来一遍遍历，把空格的index前头的item怎么怎么处理
### 太麻烦。因为如果遇到“Hello w   ”后面全是空格，就很难搞
### 新方法是找到最后一个空格的位置
### 然后从最后一个空格开始数字母的个数
