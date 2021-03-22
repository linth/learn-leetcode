"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Reference:
    - https://leetcode.com/problems/two-sum/
"""
from typing import List


class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)

        for i, v in enumerate(nums):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
    
    def twoSum2(self, nums, target):
        d = {}

        for index, value in enumerate(nums):
            diff = target - value
            if diff not in d:
                d[value] = index
            else:
                return [d[diff], index]

    # def maxValueTwoSum(self, nums):
    #     """ get max value for two numbers in an array. """
    #     max_val = 0

    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if max_val <= nums[i] + nums[j]:
    #                 max_val = nums[i] + nums[j]
    #     return max_val


if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9

    s = Solution()
    res = s.twoSum2(nums, target)
    # res = s.maxValueTwoSum(nums)
    print('res', res)
    
