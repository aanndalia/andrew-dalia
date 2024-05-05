'''
543. Diameter of Binary Tree
Solved
Easy
Topics
Companies
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.



Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1


Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
'''

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    max_diameter = 0

    def get_height(root):
        nonlocal max_diameter
        if not root:
            return -1

        left_height = get_height(root.left)
        right_height = get_height(root.right)
        diameter = left_height + right_height + 2
        max_diameter = max(max_diameter, diameter)

        # height
        return max(left_height, right_height) + 1

    if not root:
        return 0

    get_height(root)
    return max_diameter