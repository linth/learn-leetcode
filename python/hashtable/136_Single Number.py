"""
Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?


Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Reference
    - https://leetcode.com/problems/single-number/
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]):
        # Runtime: 140 ms, faster than 42.39%, Memory Usage: 16.7 MB, less than 23.47%
        """ 較佳解法 """
        d, res = {}, None
        
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for i,v in d.items():
            if v == 1:
                res = i
        return res


if __name__ == '__main__':
    nums = [4,1,2,1,2]

    s = Solution()
    res = s.singleNumber(nums)
    print('res', res)


