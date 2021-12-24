# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 12:59:42 2021

@author: m3406
"""
#My answer
class Solution(object):
    def romanToInt(self, s):
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,
               "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        lis = list(dic.keys())[::-1]
        suma = 0
        for i in lis :
            if  i in s :
                cnt = s.count(i)
                suma += dic[i]*cnt
                s = s.replace(i, "0")
        return(suma)


#Sample1
class Sample(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mydict = {'I':1, 'V':5, 'X':10 , 'L':50, 'C':100, 'D':500, 'M':1000}
        finalnum = 0
        for i in range(len(s)-1):
            if mydict[s[i]] < mydict[s[i+1]]:
                finalnum -= mydict[s[i]]
            else:
                finalnum += mydict[s[i]]
        finalnum += mydict[s[-1]]
        return finalnum