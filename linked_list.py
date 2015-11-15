# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 20:47:58 2014

@author: stree_001
"""

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self._head = None
    
    def is_empty(self):
        return self._head == None
        
    def append_item(self, value):
        if self.is_empty():
            self._head = Node(value)
        else:
            itr = self._head
            while itr.next != None:
                itr = itr.next
                
            itr.next = Node(value)
            itr.next.next = None
    
    def delete_item(self, value):
        if self.is_empty():
            return None
        
        if self._head.data == value:
            tmp = self._head
            self._head = self._head.next
            del tmp
            
        itr = self._head
        while itr.next != None:
            if itr.next.data == value:
                tmp = itr.next
                itr.next = itr.next.next
                del tmp
                return
            itr = itr.next
                
        return None
        
    def print_list(self):
        itr = self._head
        while itr.next != None:
            print itr.data,
            itr = itr.next
        
        print itr.data
        
    def length(self):
        count = 0
        itr = self._head
        while itr.next != None:
            count += 1
            itr = itr.next
            
        return count + 1
     
    def reverse_list(self):
        before = None
        current = self._head
        after = self._head.next
         
        while after != None:
            current.next = before
            before = current
            current = after
            after = after.next
             
        current.next = before
        self._head = current
    
    def get_node(self, value):
        itr = self._head
        while itr != None:
            if itr.data == value:
                return itr
            itr = itr.next
            
        return None
    
    # delete node given ptr to that node    
    def delete_node_at(self, ptr):
        if ptr == None:
            return None
            
        ptr.data = ptr.next.data
        tmp = ptr.next
        ptr.next = ptr.next.next
        del tmp
        
    def partition_list_pivot(self, pivot):
        itr = self._head
        less = LinkedList()
        more = LinkedList()
        while itr != None:
            if itr.data < pivot:
                less.append_item(itr.data)
            else:
                more.append_item(itr.data)
            itr = itr.next
        
        #less.next = more
        
        less.print_list()
        more.print_list()
        
    def get_head(self):
        return self._head
        
    def set_head(self, node):
        self._head = node
        
    
def reverse_add(l1, l2):
    if l1.is_empty():
        return l2
    if l2.is_empty():
        return l1
    
    output = LinkedList()
    carry = 0
    itr1 = l1.get_head()
    itr2 = l2.get_head()
    while itr1 != None:
        dig_sum = carry
        if itr1 != None:
            dig_sum += itr1.data
            itr1 = itr1.next
        if itr2 != None:
            dig_sum += itr2.data
            itr2 = itr2.next
        carry = dig_sum / 10
        digit = dig_sum % 10
        output.append_item(digit)
        
    return output
            
def forward_add(l1, l2):
    len_l1 = l1.length()
    len_l2 = l2.length()

    if len_l1 < len_l2:
        l1 = add_zeros(l1, len_l1, len_l2)
    else:
        l2 = add_zeros(l2, len_l2, len_l1)
    
    print "fa", l1.print_list()
    print "fa", l2.print_list()
    output = LinkedList()
    carry = 0
    itr1 = l1.get_head()
    itr2 = l2.get_head()
    while itr1 != None:
        dig_sum = carry
        if itr1 != None:
            dig_sum += itr1.data
            itr1 = itr1.next
        if itr2 != None:
            dig_sum += itr2.data
            itr2 = itr2.next
        carry = dig_sum / 10
        digit = dig_sum % 10
        output.append_item(digit)
        
    return output
    
def add_zeros(l, len_list, target_len):
    if target_len <= len_list:
        return
        
    num_zeros = target_len - len_list
    
    #l_iter = l.get_head()
    
    new_head = Node(0)
    itr = new_head
    for _ in xrange(num_zeros - 1):
        itr.next = Node(0)
    itr.next = l.get_head()
    l.set_head(new_head)
    
def main():
    l = LinkedList()
    l.append_item(3)
    l.append_item(6)
    l.append_item(1)
    
    l.print_list()
    print "length", l.length()
    l.delete_item(6)
    
    l.print_list()
    
    l.delete_item(3)
    l.print_list()
    
    arr = [2,4,6,3,8,4,23,32, 22, 65, 64, 46, 29, 98, 66,87]
    for num in arr:
        l.append_item(num)
        
    l.print_list()
    
    l.reverse_list()
    l.print_list()
    
    l.delete_node_at(l.get_node(23))
    
    l.print_list()
    
    l.partition_list_pivot(64)
    l.print_list()
    
    # add 2 linked lists in reverse notation (127 + 486)
    l1 = LinkedList()
    for num in [7,2,1]:
        l1.append_item(num) 
    
    l2 = LinkedList()
    for num in [8,4]:
        l2.append_item(num)
        
    output_list = reverse_add(l1, l2)
    output_list.reverse_list()
    output_list.print_list()
    
    #forward_add(l1,l2)
    
    
main()
                
                
        
    