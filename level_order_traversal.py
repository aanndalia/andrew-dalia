'''
102. Binary Tree Level Order Traversal
Solved
Medium
Topics
Companies
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return None

    res = []
    max_height = -1
    q = [(root, 0)]
    while q:
        cur_node, cur_height = q.pop(0)
        if cur_node.left:
            q.append((cur_node.left, cur_height + 1))

        if cur_node.right:
            q.append((cur_node.right, cur_height + 1))

        if cur_height > max_height:
            max_height = cur_height
            res.append([cur_node.val])
        else:
            res[cur_height].append(cur_node.val)

    return res