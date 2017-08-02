    void Swap(int &a, int &b)  
    {  
        if (a != b)  
        {  
            a ^= b;  
            b ^= a;  
            a ^= b;  
        }  
    }  
    
1.   a = a^b
2.   b = b^a   ->  b = b^(a^b)=a
3.   a = a^b   ->  a = (a^b)^b = (a^b)^a = b
      
这样就把a和b交换了
      
但是我经常混淆a和b的赋值，为了更方便地理解：
  
      a1 = a ^ b
      b1 = b ^ a1
      a2 = a1 ^ b1
      
      
