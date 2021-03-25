"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.


Example 1:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

Example 2:
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.

Note:
The number of nodes in the given list will be between 1 and 100.

# Reference 
    - https://leetcode.com/problems/middle-of-the-linked-list/
    - https://www.youtube.com/watch?v=u0vcs_jZ1A8
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode):
        # Runtime: 24 ms, faster than 94.81%, Memory Usage: 14.3 MB, less than 45.40%
        """ 較佳解法 """
        a = []
        
        while head:
            a.append(head)
            head = head.next        
        return a[int(len(a) / 2)]


# if __name__ == '__main__':
#     pass

