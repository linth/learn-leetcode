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
    def twoSum0(self, nums, target):
        """
        nums = [2, 7, 11, 15], target = 9

        :param nums:
        :param target:
        :return:
        """
        pass

    def twoSum(self, nums, target):
        """
        brute force.

        :param nums:
        :param target:
        :return:
        """
        n = len(nums)

        for i, v in enumerate(nums):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
    
    def twoSum2(self, nums, target):
        """
        較佳解法

        :param nums:
        :param target:
        :return:
        """
        d = {}

        for index, value in enumerate(nums):
            diff = target - value
            if diff not in d:
                d[value] = index
            else:
                return [d[diff], index]

    def twoSum3(self, nums, target):
        """
        :param nums:
        :param target:
        :return:
        """
        # two points.
        begin, end = 0, len(nums) - 1

        nums_index = [(v, index) for index, v in enumerate(nums)]
        nums_index.sort()
        # print('nums_index', nums_index)

        while begin < end:
            curr = nums_index[begin][0] + nums_index[end][0]

            if curr == target:
                return [nums_index[begin][1], nums_index[end][1]]
            elif curr < target:
                begin += 1
            else:
                end -= 1

    def twoSum4(self, nums, target):
        """ two-pass hash table. """
        pass

    def twoSum5(self, nums, taget):
        """ one-pass hash table. """
        pass

    # def maxValueTwoSum(self, nums):
    #     """ get max value for two numbers in an array. """
    #     max_val = 0

    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if max_val <= nums[i] + nums[j]:
    #                 max_val = nums[i] + nums[j]
    #     return max_val


if __name__ == '__main__':
    nums = [2, 11, 7, 15]
    target = 9

    s = Solution()
    # res = s.twoSum(nums, target)
    res = s.twoSum2(nums, target)
    # res = s.twoSum3(nums, target)
    # res = s.maxValueTwoSum(nums)
    print('res', res)
