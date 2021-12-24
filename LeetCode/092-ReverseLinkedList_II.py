# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 21:01:03 2021

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


#My Ans
class Solution:
    def reverseBetween(self, head, left: int, right: int):
        if not head or not head.next:
            return head
        lis = []
        while head:
            lis.append(head.val)
            head = head.next
        
        lis = lis[0:left-1] + lis[left-1:right][::-1] + lis[right:]
        ans_node = curr_node = ListNode(0)
        
        for i in lis:
            curr_node.next = ListNode(i)
            curr_node = curr_node.next
        
        return ans_node.next
    
#Sample 
#https://leetcode.com/problems/reverse-linked-list-ii/discuss/1167109/Python3-One-pass-iterative-solution-beats-95.50-(with-figure-explanation)
class Sample:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or not head.next or left == right:
            return head
        
        dummy_head = ListNode(val=-1, next=head)
        p_prev = dummy_head
        
        # Iterate p_prev to the (left-1)-th node
        for _ in range(left - 1):
            p_prev = p_prev.next
            
        p_cur = p_prev.next # p_cur is at the left-th node
        
        # Within the reverse part, iteratively move the next node of p_cur to the beginning
        for _ in range(right - left):
            p_next = p_cur.next
            p_cur.next = p_next.next
            p_next.next = p_prev.next
            p_prev.next = p_next
        
        return dummy_head.next