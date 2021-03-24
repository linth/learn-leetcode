"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Example 1:
    Input: l1 = [1,2,4], l2 = [1,3,4]
    Output: [1,1,2,3,4,4]

Example 2:
    Input: l1 = [], l2 = []
    Output: []

Example 3:
    Input: l1 = [], l2 = [0]
    Output: [0]

Constraints:
    - The number of nodes in both lists is in the range [0, 50].
    - -100 <= Node.val <= 100
    - Both l1 and l2 are sorted in non-decreasing order.

Reference:
    - https://leetcode.com/problems/merge-two-sorted-lists/
    - https://www.youtube.com/watch?v=Z7VOBq6S5n8
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        # Runtime: 32 ms, faster than 92.07%
        """ 較佳解法 """
        # dumy的ListNode主要是提供return之後給的完整地linked list.
        curr = dumy = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dumy.next
        

# if __name__ == '__main__':
    # l1 = [1, 2, 4]
    # l2 = [1, 3, 4]

    # s = Solution()
    # res = s.mergeTwoLists(l1, l2)
    # print(f'the result = {res}')
