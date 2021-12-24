# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 03:48:24 2021

@author: m3406
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def print_all(node):
    while node : 
        print(node.val)
        node = node.next
        
#My Ans
class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head
        tic = head
        while tic.next:
            temp = tic.val
            if tic.next.val== temp:
                tic.next = tic.next.next
            else : 
                tic = tic.next
        return head 