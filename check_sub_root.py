'''
572. Subtree of Another Tree
Solved
Easy
Topics
Companies
Hint
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.



Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false


Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
'''

def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def check_match(root, sub_root):
        if root is None and sub_root is None:
            return True

        if root is None or sub_root is None:
            return False

        if root.val != sub_root.val:
            return False

        left_match = check_match(root.left, sub_root.left)
        right_match = check_match(root.right, sub_root.right)
        if not left_match or not right_match:
            return False

        return True

    def check_subtree(root, sub_root):
        if root is None and sub_root is None:
            return True

        if root is None or sub_root is None:
            return False

        if root.val == sub_root.val:
            if check_match(root, sub_root):
                return True

        is_left_subtree = check_subtree(root.left, sub_root)
        is_right_subtree = check_subtree(root.right, sub_root)

        if is_left_subtree or is_right_subtree:
            return True

        return False

    res = check_subtree(root, subRoot)
    return res