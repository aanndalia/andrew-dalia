# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 06:44:12 2015

@author: stree_001
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l2 == None:
            return l1
        if l1 == None:
            return l2
            
        digit_val = (l1.val + l2.val) % 10;
        remainder = (l1.val + l2.val) / 10;
        result_list = ListNode(digit_val)
        i1 = l1
        i2 = l2
        r = result_list
        while i1 != None or i2 != None:
            digit_val = (i1.val + i2.val + remainder) % 10
            #new_val = digit_val + remainder
            r.next = ListNode(digit_val)
            remainder = digit_val / 10;
            i1 = i1.next
            i2 = i2.next
            r = r.next
            
        if i1 == None:
            while i2 != None:
                digit_val = (i2.val + remainder) % 10
                remainder = digit_val / 10
                r.next = ListNode(digit_val)
                r = r.next
                i2 = i2.next
        
        if i2 == None:
            while i1 != None:
                digit_val = (i1.val + remainder) % 10
                remainder = digit_val / 10
                r.next = ListNode(digit_val)
                r = r.next
                i1 = i1.next
        
        if remainder != 0:
            r.next = ListNode(remainder)
        
        return result_list
            

def main():
    l1 = ListNode(3)
    l1.next = ListNode(7)
    l1.next.next = ListNode(4)
    l2 = ListNode(8)
    l2.next = ListNode(4)
    l2.next.next = ListNode(2)
    # 374 + 842 -> 1216
    s = Solution()
    s.addTwoNumbers()
    
main()