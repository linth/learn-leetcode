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
    def runningSum0(self, nums):
        pass

    def runningSum(self, nums: List[int]) -> List[int]:
        """ 較佳解法 """
        sum = 0
        new_arr = [] # 你也可以使用取代方式來進行，這樣就可以不用額外新增新的array

        for i in nums:
            sum += i
            new_arr.append(sum)
        return new_arr


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    s = Solution()
    res = s.runningSum(nums)
    print(f'the result is {res}')

    # res0 = s.runningSum0(nums)
    # print(f'the result is {res0}')
