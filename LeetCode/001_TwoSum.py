# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 23:49:38 2021

@author: m3406
"""
nums = [2,4,11,3] 
target = 6

#My ANS
class Solution:
    def twoSum(self,nums, target):
        diff = None 
        i = 0
        while True : 
            diff = target - nums[0]
            del nums[0]
            if diff in nums:
                ans = [i,i+1+nums.index(diff)]
                break
            i+=1
        return(ans)


#Sample
class Sample:
    def twoSum(self,nums, target):
            hashed = {}
            for i,n in enumerate(nums):
    	        x = target - n
    	        if x in hashed:
    		        return[hashed[x],i]
    	        hashed[n] = i
    
