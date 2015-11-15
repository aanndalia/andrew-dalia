# -*- coding: utf-8 -*-
"""
Created on Tue Dec 02 08:31:53 2014

@author: stree_001
"""

# implement queue with 2 stacks
class TwoStackQueue:
    def __init__(self):
        self._s1 = []
        self._s2 = []
        
    def push(self, x):
        self._s1.append(x)
        
    def pop(self):
        if len(self._s2) > 0:
            return self._s2.pop()
        else:
            if len(self._s1) > 0:
                for item in self._s1:
                    self._s2.append(self._s1.pop())
                return self._s2.pop()
            else:
                print "ERROR: nothing to pop"
                return None
    
def main():
    q = TwoStackQueue()
    
    while(True):
        type_inp = raw_input("Would you like to push or pop or quit? ")
        
        if type_inp == "push":
            val_inp = raw_input("What item? ")
            q.push(val_inp)
            print "Pushed", val_inp
        elif type_inp == "pop":
            print "Popped", q.pop()
        elif type_inp == "quit":
            break
        else:
            print "Invalid command"
            
main()