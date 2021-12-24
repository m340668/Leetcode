# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 05:07:19 2021

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

def Creat_node(lis):
    head = node = ListNode(0)
    for i in lis:
        node.next = ListNode(i)
        node = node.next
    return head.next

head = Creat_node([1,4,3,0,2,5,2])
x = 3

#My Ans
class Solution:
    def partition(self, head, x):
        if not head or not head.next:
            return head
        
        curr_node = pre_node = ans_node = ListNode(-201)
        curr_node.next = head
        
        while curr_node.next and curr_node.next.val < x :
            curr_node = curr_node.next
            pre_node = pre_node.next

        
        target_node = curr_node.next
        curr_node = curr_node.next

        
        while curr_node and curr_node.next:
            if curr_node.next.val < x :
                pre_node.next = curr_node.next
                pre_node = pre_node.next
                curr_node.next = curr_node.next.next
                pre_node.next = target_node
            else:    
                curr_node = curr_node.next
        
        return ans_node.next



#Sample
class Sample:
    def partition(self, head: ListNode, x: int) -> ListNode:
        fdum, bdum = ListNode(0), ListNode(0)
        front, back, curr = fdum, bdum, head
        while curr:
            if curr.val < x:
                front.next = curr
                front = curr
            else:
                back.next = curr
                back = curr
            curr = curr.next
        front.next, back.next = bdum.next, None
        return fdum.next