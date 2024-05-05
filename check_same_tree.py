'''
100. Same Tree
Solved
Easy
Topics
Companies
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false


Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
'''

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def check_same(x, y):
        if not x and not y:
            return True

        if not x or not y:
            return False

        if x.val != y.val:
            return False

        check_left = check_same(x.left, y.left)
        check_right = check_same(x.right, y.right)

        if check_left and check_right:
            return True

        return False

    res = check_same(p, q)
    return res