"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.


Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]


Reference:
- https://leetcode.com/problems/running-sum-of-1d-array
"""
from typing import List


class Solution:
    @staticmethod
    def runningSum(nums: List[int]) -> List[int]:
        sum = 0
        new_arr = []

        for i in nums:
            sum += i
            new_arr.append(sum)
        return new_arr


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    s = Solution()
    res = s.runningSum(nums)
    print(f'the result is {res}')
