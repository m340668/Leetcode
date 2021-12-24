# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 00:50:08 2021

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

head = ListNode(val = 1) 
head.next = ListNode(val = 2,next = ListNode(val = 3, next = ListNode(4)))

#Sample
class Solution:
    def swapPairs(self, head):
        curr_node = head
        next_node = head and head.next
        new_head = next_node or curr_node
        
        while curr_node and next_node:
            # Grab the next pair of nodes
            third_node = next_node.next
            fourth_node = third_node and third_node.next
            # Flip first pair, shift
            next_node.next = curr_node
            curr_node.next = fourth_node or third_node
            curr_node, next_node = third_node, fourth_node
            
        return new_head