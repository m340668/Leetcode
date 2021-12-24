# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 22:54:45 2021

@author: m3406
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#My Ans
class Solution:
    def sortedListToBST(self, head):
        if not head:
            return head
        
        #Create list
        node_list = []
        while head:
            node_list.append(head.val)
            head = head.next
        
        #TreeNode
        def CreateTree(node_list):
            if not node_list:
                return None
            
            mid = len(node_list)//2
            root = TreeNode(node_list[mid])
            root.left = CreateTree(node_list[:mid])
            root.right = CreateTree(node_list[mid+1:])
            return root
        
        return CreateTree(node_list)

#Sample
class Sample:
    def sortedListToBST(self, head: ListNode) -> TreeNode:        
        if not head:
            return         
        if not head.next:            
            return  TreeNode(head.val)        
        pre , slow , fast = None, head, head
        while fast and fast.next:                                
            pre = slow
            slow = slow.next
            fast = fast.next.next            
        pre.next = None                
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root
