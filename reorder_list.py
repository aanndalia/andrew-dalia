'''
143. Reorder List
Solved
Medium
Topics
Companies
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]


Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
'''


def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if not head or not head.next:
        return

    slow = head
    fast = head.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    head_right = slow.next
    cur = head_right
    slow.next = None
    prev = None
    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp

    left = head
    right = prev
    # print(left, right)
    while left and right:
        tmp_left = left.next
        tmp_right = right.next
        left.next = right
        right.next = tmp_left
        left = tmp_left
        right = tmp_right

    return head