# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:33:43 2021

@author: m3406
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#My Ans
class Solution:
    def addTwoNumbers(self, l1, l2) :
        ans = ListNode()
        count = 0
        tic = ans
        while l1 and l2:
            
            x = l1.val + l2.val +count
            count = 0
            if x<10:
                tic.next = ListNode(x)
            else:
                tic.next = ListNode(x % 10)
                count += 1
            
            tic = tic.next
            l1, l2 = l1.next, l2.next
        
        if l1 :
            while l1 :
                x = l1.val + count
                count = 0

                if x<10:
                    tic.next = ListNode(x)
                else:
                    tic.next = ListNode(x % 10)
                    count += 1
                tic = tic.next
                l1 = l1.next
        if l2 :
            while l2 :
                x = l2.val + count
                count = 0

                if x<10:
                    tic.next = ListNode(x)
                else:
                    tic.next = ListNode(x % 10)
                    count += 1
                tic = tic.next
                l2 = l2.next
        
        if count > 0 :
            tic.next = ListNode(count)
        
        return ans.next 

#Sample
class Sample:
    def addTwoNumbers(self, l1, l2) :
        def traverse(l1, l2, carry):
            if not l1 and not l2 and not carry:
                return None
            tmp = 0
            if l1:
                tmp+=l1.val
                l1 = l1.next
            if l2:
                tmp+=l2.val
                l2 = l2.next
            if carry:
                tmp+=1
                carry = False
            if tmp>=10: carry = True
            return ListNode(val = tmp%10, next=traverse(l1, l2, carry))
            
        return traverse(l1, l2, False)