"""
Given head which is a reference node to a singly-linked list. 
The value of each node in the linked list is either 0 or 1. 
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Example 1:
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:
Input: head = [0]
Output: 0

Example 3:
Input: head = [1]
Output: 1

Example 4:
Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880

Example 5:
Input: head = [0,0]
Output: 0

Constraints:
- The Linked List is not empty.
- Number of nodes will not exceed 30.
- Each node's value is either 0 or 1.

# Reference
    - https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode):
        # Runtime: 32 ms, faster than 62.21%, Memory Usage: 14.3 MB, less than 41.23%
        """ 較佳解法 """
        ans = 0
        
        while head:
            ans = ans * 2 + head.val
            head = head.next
        return ans


# if __name__ == '__main__':
#     pass

