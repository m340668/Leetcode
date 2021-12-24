# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 17:04:44 2021

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
    node = ListNode(0)
    for i in range(len(list)):
        node.next = ListNode(lis[i])
    return node.next


#My Ans
class Solution:
    def deleteDuplicates(self, head):
        
        if not head or not head.next:
            return head
       
    #Get Right Head 
        new_head = ListNode(101,head)
        curr_node = new_head
        
        while curr_node.next and curr_node.next.next :
            second_node = curr_node.next
            if second_node.val == second_node.next.val:
                while second_node.next and second_node.val == second_node.next.val:
                    second_node = second_node.next
                curr_node.next = second_node.next
            else:
                curr_node = curr_node.next
   
        return new_head.next
    
#Sample
class Sample:
    def deleteDuplicates(self, head):
        dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next