'''
104. Maximum Depth of Binary Tree
Solved
Easy
Topics
Companies
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''

def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    max_height = 1
    q = [(root, 1)]
    while q:
        node, height = q.pop(0)
        if node.left:
            q.append((node.left, height + 1))
        if node.right:
            q.append((node.right, height + 1))

        max_height = max(max_height, height)

    return max_height