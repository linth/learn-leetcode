"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []


Constraints:
- The number of nodes in the list is in the range [0, 104].
- 1 <= Node.val <= 50
- 0 <= k <= 50

# Reference
    - https://leetcode.com/problems/remove-linked-list-elements/
    - https://www.youtube.com/watch?v=nwXxL2KtV1Y
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int):
        # Runtime: 76 ms, faster than 21.56%, Memory Usage: 17.3 MB, less than 24.64%
        """ 較佳解法 """
        dummy = ListNode(float('-inf'))
        dummy.next = head
        
        prev, curr = dummy, dummy.next
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next


# if __name__ == '__main__':
#     pass

