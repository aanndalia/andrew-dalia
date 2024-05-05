'''
199. Binary Tree Right Side View
Solved
Medium
Topics
Companies
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.



Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    res = []
    q = [(root, 0)]
    max_height = -1
    while q:
        cur_node, cur_height = q.pop(0)
        if cur_node.left:
            q.append((cur_node.left, cur_height + 1))
        if cur_node.right:
            q.append((cur_node.right, cur_height + 1))

        if cur_height > max_height:
            max_height = cur_height
            res.append(cur_node.val)
        else:
            res[cur_height] = cur_node.val

    return res