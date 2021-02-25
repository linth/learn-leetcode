"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Constraints:
1. The number of nodes in the list is the range [0, 5000].
2. -5000 <= Node.val <= 5000

Reference:
    - https://leetcode.com/problems/reverse-linked-list/
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        print(f'the origin ListNode: {head}')
        # prev_node = None
        # curr_node = head
        # while curr_node:
        #     next_node = curr_node.next # Remember next node
        #     curr_node.next = prev_node  # REVERSE! None, first time round.
        #     prev_node = curr_node  # Used in the next iteration.
        #     curr_node = next_node  # Move to next node.
        # head = prev_node
        return head


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]

    s = Solution()
    res = s.reverseList(head)
    print(f'after reversing, the result = {res}')
        