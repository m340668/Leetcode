# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 01:29:37 2021

@author: m3406
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list1 = ListNode(val = 1) 
list1.next = ListNode(val = 2,next = ListNode(val = 4))

list2 = ListNode(val = 1) 
list2.next = ListNode(val = 3,next = ListNode(val = 4))

#My answer
class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return(list2)
        if not list2:
            return(list1)
        ans = ListNode()
        while True :
            tic = ans
            while tic.next:
                tic = tic.next
            if list1.val < list2.val:
                tic.next = ListNode(list1.val)
                if not list1.next:
                    tic.next.next = list2
                    break
                list1 = list1.next
            
            else: 
                tic.next = ListNode(list2.val)
                if not list2.next:
                    tic.next.next = list1
                    break
                list2 = list2.next
        return(ans.next)

#SAMPLE
class SAMPLE:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy = ListNode(0)
        head  = dummy
            
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
                head = head.next
            else:
                head.next = l2
                l2 = l2.next
                head = head.next  
		# Checking if either of the list remains after the while loop		
        if l1:
            head.next = l1
        elif l2:
            head.next = l2
            
        return dummy.next