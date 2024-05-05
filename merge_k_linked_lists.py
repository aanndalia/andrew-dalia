'''
23. Merge k Sorted Lists
Solved
Hard
Topics
Companies
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None

    head = ListNode()
    cur_ptr = head
    ptr_list = [llist for llist in lists]
    while True:
        any_ptr = False
        min_val = float('inf')
        min_idx = 0
        for i, ptr in enumerate(ptr_list):
            if not ptr:
                continue

            any_ptr = True
            if ptr.val < min_val:
                min_val = ptr.val
                min_idx = i

        if not any_ptr:
            break

        cur_ptr.next = ptr_list[min_idx]
        ptr_list[min_idx] = ptr_list[min_idx].next
        cur_ptr = cur_ptr.next

    res = head.next
    return res