"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

Reference:
    - https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        pass


if __name__ == '__main__':
    st = "()[]{}"
    s = Solution()
    res = s.isValid(st)
    print('res', res)

