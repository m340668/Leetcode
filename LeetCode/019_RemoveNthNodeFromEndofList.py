# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 17:43:42 2021

@author: m3406
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#My Ans
class Solution:
    def removeNthFromEnd(self, head, n) :
        l = 1
        tic = head
        while tic.next : 
            l+=1
            tic = tic.next
        
        tic = head
        if l-n == 0:
            return head.next
        
        for i in range(l-n-1):
            tic = tic.next
        
        tic.next = tic.next.next
        return head