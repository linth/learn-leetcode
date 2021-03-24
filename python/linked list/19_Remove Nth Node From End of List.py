"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

problem concept:
    - 利用一個指標尋找結尾、一個指標尋找要刪除的那個 Node 的前一個人是誰。
      基本上就是讓找結尾的指標先走了 n 個節點後，再開始讓尋找要刪除的那個 Node 
      的前一個人的指標開始從頭一起走就可以搜尋到了。

Reference:
    - https://leetcode.com/problems/remove-nth-node-from-end-of-list/
    - https://www.youtube.com/watch?v=F5kFspTdW1I
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        """ 較佳解法 """
        # Runtime: 28 ms, Memory: 14.3 MB
        # two pointers.
        fast = slow = head
        
        # 如何從頭開始算，找到整個linked list的倒數第二個
        for _ in range(n):
            fast = fast.next
            
        if not fast:
            return head.next
        
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


# if __name__ == '__main__':
#     head = [1, 2, 3, 4, 5]
#     n = 2
#     s = Solution()
#     res = s.removeNthFromEnd(head, n)
#     print('res', res)

