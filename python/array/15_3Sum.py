"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.


Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Constraints:
0 <= nums.length <= 3000
-105 <= nums[i] <= 105

Reference:
    - https://leetcode.com/problems/3sum/
    - https://medium.com/jacky-life/leetcode-3sum-bb1deec8ba31
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []

        nums.sort()
        ans_list = []

        frist = 0
        second = frist + 1
        third = nums.length - 1

        for frist in range(0, len(nums)):
            if nums[frist] + nums[second] + nums[third] == 0:
                res.append([nums[frist], nums[second], nums[third]])
            elif nums[frist] + nums[second] + nums[third] < 0:
                second += 1
            else:
                third -= 1



if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    res = s.threeSum(nums)

