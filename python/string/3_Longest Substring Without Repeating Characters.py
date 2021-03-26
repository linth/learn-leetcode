"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

Reference:
    - https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s: str):
        """ hash map. """
        d = {}
        j, ans = 0, 0
        for i in range(len(s)):
            if s[i] in d:
                j = max(d[s[i]], j)
            ans = max(ans, i-j+1)
            d[s[i]] = i+1
        return ans

    def lengthOfLongestSubstring2(self, s: str):
        """ brute force. """
        # https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/
        pass


if __name__ == '__main__':
    st = "abcabcbb"
    s = Solution()
    res = s.lengthOfLongestSubstring(st)
    print('res', res)


