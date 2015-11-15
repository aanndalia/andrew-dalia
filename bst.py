# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 23:08:06 2014

@author: stree_001
"""

import random
from collections import deque

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        
    def insert_item(self, item):
        if self.root == None:
            self.root = Node(item)
        else:
           self._insert(item, self.root)
            
    def _insert(self, item, node):
        if item < node.data:
            if node.left == None:
                node.left = Node(item)
            else:
                self._insert(item, node.left)
        else:
            if node.right == None:
                node.right = Node(item)
            else:
                self._insert(item, node.right)
                
    def build_tree(self, lst):
        for item in lst:
            self.insert_item(item)
            
    def find_item(self, item):
        if self.root == None:
            return None
        else:
            return self._find(item, self.root)
            
    def _find(self, item, node):
        if item == node.data:
            return node
        
        if item < node.data:
            if node.left == None:
                return None
            else:
                return self._find(item, node.left)
        else:
            if node.right == None:
                return None
            else:
                return self._find(item, node.right)
                
    def is_empty(self):
        if self.root == None:
            return True
        else:
            return False
            
    def preorder_traversal(self):
        if self.root == None:
            print "None"
        else:
           self._preorder(self.root)
            
    def _preorder(self, node):
        print node.data,
        
        if node.left != None:
            self._preorder(node.left)
        
        if node.right != None:
            self._preorder(node.right)
            
    def inorder_traversal(self):
        if self.root == None:
            print "None"
        else:
            self._inorder(self.root)
            
    def _inorder(self, node):
        if node.left != None:
            self._inorder(node.left)
            
        print node.data,
        
        if node.right != None:
            self._inorder(node.right)
            
    def postorder_traversal(self):
        if self.root == None:
            print "None"
        else:
            self._postorder(self.root)
            
    def _postorder(self, node):
        if node.left != None:
            self._postorder(node.left)
            
        if node.right != None:
            self._postorder(node.right)
            
        print node.data,
        
    def node_height(self, node):
        if self.root == None:
            return 0
            
        right_height = 0
        left_height = 0
        if node.left != None:
            left_height = self.node_height(node.left)
        if node.right != None:
            right_height = self.node_height(node.right)
        
        return max(left_height, right_height) + 1
        
    def bfs(self):
        if self.root == None:
            return
            
        q = deque([self.root])
        while len(q) > 0:
            x = q.popleft()
            print x.data,
            if x.left != None:
                q.append(x.left)
            if x.right != None:
                q.append(x.right)
                
    def dfs(self):
        if self.root == None:
            return
            
        s = [self.root]
        while len(s) > 0:
            x = s.pop()
            print x.data,
            if x.right != None:
                s.append(x.right)
            if x.left != None:
                s.append(x.left)
                
    def get_levels(self):
        q = deque([(self.root, 0)])
        level_arr = [[self.root]]
        while len(q) > 0:
            x, h = q.popleft()
            if x.left != None:
                q.append((x.left, h + 1))
                if (h+1) > (len(level_arr) - 1):
                    level_arr.append([x.left])
                else:
                    level_arr[(h+1)].append(x.left)
                    
            if x.right != None:
                q.append((x.right, h + 1))
                if (h+1) > (len(level_arr) - 1):
                    level_arr.append([x.right])
                else:
                    level_arr[(h+1)].append(x.right)
                    
        return level_arr
        
    def mirror_tree(self):
        if self.root == None:
            return
        
        # swap left and right nodes
        temp = self.root.left
        self.root.left = self.root.right
        self.root.right = temp
        
        if self.root.left != None:
            self._mirror(self.root.left)
        if self.root.right != None:
            self._mirror(self.root.right)
        
    def _mirror(self, node):
        if node.left == None and node.right == None:
            return
            
        temp = node.left
        node.left = node.right
        node.right = temp
        
        if node.left != None:
            self._mirror(node.left)
        if node.right != None:
            self._mirror(node.right)
            
    def __str__(self, node, depth=0):
        ret = ""

        # Print right branch
        if node.right != None:
            ret += node.right.__str__(depth + 1)

        # Print own value
        ret += "\n" + ("    "*depth) + str(node.value)

        # Print left branch
        if node.left != None:
            ret += node.left.__str__(depth + 1)

        return ret
        
    def get_root(self):
        return self.root
        
    def _postorder_list(self, node, lst):
        if node.left != None:
            self._postorder_list(node.left, lst)
            
        if node.right != None:
            self._postorder_list(node.right, lst)
            
        lst.append(node.data)
        
        return lst
        
    def _inorder_list(self, node, lst):
        if node.left != None:
            self._inorder_list(node.left, lst)
            
        lst.append(node.data)
        
        if node.right != None:
            self._inorder_list(node.right, lst)
            
        return lst
        
    def lowest_common_ancestor(self, x, y):
        # get inorder traversal of bst 
        inorder = self._inorder_list(self.get_root(), [])
        
        # get postorder traversal of bst
        postorder = self._postorder_list(self.get_root(), [])
        
        # get subset of bst inorder between nodes x and y
        try:
            x_ind = inorder.index(x)
            y_ind = inorder.index(y)
        except ValueError:
            return None
        
        if x_ind < y_ind:
            lower_ind = x_ind
            higher_ind = y_ind
        else:
            lower_ind = y_ind
            higher_ind = x_ind
            
        subset_inorder = inorder[lower_ind:(higher_ind + 1)]

        set_subset = set(subset_inorder)
        for j in range(len(postorder) - 1, -1, -1):
            if postorder[j] in set_subset:
                return postorder[j]
        
        return None
        
    # wrapper to check_height
    def is_balanced(self):
        if self.check_height(self.root) == -1:
            return False
        else:
            return True
        
    
    # checks height of subtrees to see if tree is balanced
    def check_height(self, root):
        if root == None:
            return 0
        
        left_height = self.check_height(root.left)
        if left_height == -1:
            return -1
        
        right_height = self.check_height(root.right)
        if right_height == -1:
            return -1
       
        diff = left_height - right_height
        if diff < -1 or diff > 1:
            return -1
            
        return max(left_height, right_height) + 1
                
    def sum_paths(self, root, target, path):
        if root == None:
            return
            
        new_sum_path = sum(path) + root.data
        
        path.append(root.data)
        
        if new_sum_path == target:
            for p in path:
                print p,
            print
        
        self.sum_paths(root.left, target, path)
        self.sum_paths(root.right, target, path)
        
    def sum_paths2(self, root, target, path):
        if root == None:
            return
            
        new_path = list(path) + [root.data]
        
        cur_sum = 0
        for i in range(len(new_path) - 1, -1, -1):
            cur_sum += new_path[i]
            if cur_sum == target:
                print new_path[i:len(new_path)]
                
        self.sum_paths2(root.left,  target, new_path)
        self.sum_paths2(root.right, target, new_path)
        
    def inorder_successor(self, node):
        if node == None:
            return None
            
        if node.right == None:
            return self.up_search(node)
            
        return self.left_search(node.right)
        
    def left_search(self, node):
        if node.left == None:
            return node
            
        return self.left_search(node.left)
        
    def up_search(self, node):
        if node.parent == None:
            return None
            
        if node.parent.left == node:
            return node.parent
            
        return self.up_search(node.parent)    
            
        
def main():
    bst = BST()
    
    bst.insert_item(5)
    bst.insert_item(3)
    
    
    #bst.build_tree([random.randint(0,1000) for _ in xrange(100)])
    bst.build_tree([6, 4, 0, 9, 18, 12, 11, 14])
    #bst.build_tree([6, 4, 0, 9])
    bst.preorder_traversal()
    print
    bst.inorder_traversal()
    print
    bst.postorder_traversal()
    print
    #bst.inorder_traversal()
    #print
    print bst.find_item(5)
    print
    
    #print "is_balanced:", bst.is_balanced(bst.get_root())
    print "is_balanced:", bst.is_balanced()
    
    print "sum paths"
    bst.sum_paths(bst.get_root(), 18, [])
    print "sum paths 2"
    bst.sum_paths2(bst.get_root(), 12, [])
    #print bst.node_height(bst.find_item(3))
    print "BFS"
    bst.bfs()
    print 
    print "DFS"
    bst.dfs()
    print
    print "height", str(bst.node_height(bst.find_item(5)))
    print
    
    for level in bst.get_levels():
        for node in level:
            print node.data,
        print 
    

    #print str(bst)
    
    bst.mirror_tree()
    print
    bst.inorder_traversal()
    print
    
    for level in bst.get_levels():
        for node in level:
            print node.data,
        print 
    
    print "lca", 
    print bst.lowest_common_ancestor(18,4)
    
    bst3 = BST()
    bst3.build_tree([7,6,9,5,1,8,4])
    
    bst4 = BST()
    bst4.build_tree([5,1,8,4])
    
    
    #bst.get_levels
    
main()
            
    
            
    