"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.


Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [], target = 0
Output: []
 

Constraints:
- 0 <= nums.length <= 200
- -109 <= nums[i] <= 109
- -109 <= target <= 109

Reference
    - https://leetcode.com/problems/4sum/
"""

class Solution:
    def fourSum(self, nums: List[int], target: int):
        pass


if __name__ == '__main__':
    nums = [1,0,-1,0,-2,2]
    target = 0

    s = Solution()
    res = s.fourSum(nums, target)
    print('res', res)
