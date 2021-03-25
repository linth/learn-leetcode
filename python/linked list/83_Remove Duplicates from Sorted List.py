"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.


Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:
- The number of nodes in the list is in the range [0, 300].
- -100 <= Node.val <= 100
- The list is guaranteed to be sorted in ascending order.


# Reference
    - https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode):
        # Runtime: 36 ms, faster than 93.79%, Memory Usage: 14.2 MB, less than 84.54%
        """ 較佳解法 """
        curr = head
        
        while curr:
            runner = curr.next
            while runner and curr.val == runner.val:
                runner = runner.next
            curr.next = runner
            curr = runner
        return head

    def deleteDuplicates2(self, head: ListNode):
        # Runtime: 40 ms, faster than 80.03%, Memory Usage: 14 MB, less than 99.46%
        curr = nxt = head
        
        while curr:
            nxt = curr.next
            while nxt and curr.val == nxt.val:
                nxt = nxt.next
            curr.next = nxt
            curr = nxt
        return head


# if __name__ == '__main__':
#     pass

