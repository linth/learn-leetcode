"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.


Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false
 

Constraints:
1 <= n <= 231 - 1

Reference
    - https://leetcode.com/problems/happy-number/
    - https://www.polarxiong.com/archives/LeetCode-202-happy-number.html
"""

class Solution:
    def isHappy(self, n: int):
        # Runtime: 32 ms, faster than 83.59%, Memory Usage: 14.2 MB, less than 50.94%
        """ 較佳解法 """
        s = set()

        while n != 1 and n not in s:
            s.add(n)
            sum = 0

            while n:
                sum += (n % 10)**2
                n //= 10
            n = sum
        return n == 1


if __name__ == '__main__':
    n = 19

    s = Solution()
    res = s.isHappy(n)
    print('res', res)
    
