# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 03:40:49 2021

@author: m3406
"""
x = 10

#My ANS
def isPalindrome(self, x):
    if x<0:
        return(False)
    else : 
        st = [a for a in str(x)]
        st2 = st.copy()
        st.reverse()
        return(st2 == st)
    
#Sample1
class Sample1:
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]

#Sample2
class Sample2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        rev_num = 0
        while(x):
            rev_num = rev_num*10 + x%10
            x = int(x/10)
        if rev_num == num:
            return True
        return False