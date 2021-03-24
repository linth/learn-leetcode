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
    - https://www.youtube.com/watch?v=QuWBvSx9DeI

Others:
    - (stack and heap底層概念) https://nwpie.blogspot.com/2017/05/5-stack-heap.html
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # prev, curr, head, nxt 皆為reference
        prev, curr, nxt = None, head, None
        
        while curr:
            nxt = curr.next
            
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


# if __name__ == '__main__':
#     head = [1, 2, 3, 4, 5]
#     s = Solution()
#     res = s.reverseList(head)
#     print(f'after reversing, the result = {res}')
        