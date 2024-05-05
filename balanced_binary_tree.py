'''
110. Balanced Binary Tree
Solved
Easy
Topics
Companies
Given a binary tree, determine if it is
height-balanced
.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''

def isBalanced(root: Optional[TreeNode]) -> bool:
    def get_height(root):
        if root is None:
            return 0

        left_height = get_height(root.left)
        right_height = get_height(root.right)
        if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
            return -1

        height = max(left_height, right_height) + 1
        return height

    if root is None:
        return True

    res = get_height(root) >= 0
    return res