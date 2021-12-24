# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 18:04:21 2021

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
head.next = ListNode(val = 2,next = ListNode(val = 3, next = ListNode(val = 4,next = ListNode(5))))
k = 2

#My Ans
class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head
        
        tic = head
        
        n = 1
        while tic.next:
            tic = tic.next
            n += 1
        
        k = k % n
        
        if k == 0:
            return head
        
        tic.next = head
        i = 0
        tic = tic.next
        while True:
            i += 1
            tic = tic.next
            if i == n-k:
                start = tic
            
            if i == 2*n-k-1:
                tic.next = None
                break
        
        return start

#Sample
class Sample:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head:
            node = head
            nodeList = []

            while node:
                nodeList.append(node)
                node = node.next

            if (rotation := k % len(nodeList)):
                head = nodeList[-rotation]
                nodeList[-1].next = nodeList[0]
                tail = nodeList[-rotation-1]
                tail.next = None

        return head