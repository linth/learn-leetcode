"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

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
    def threeSum(self, nums):
        n = len(nums)

        if n < 3:
            return []
        nums.sort()
        res = []

        for first in range(0, n-2, 1):
            second = first + 1
            third = n - 1

            while(second != third):
                total = (nums[first] + nums[second])
                total = total + nums[third]

                if total == 0:
                    res.append([nums[first], nums[second], nums[third]])
                    while second < third:
                        second += 1
                        if (nums[second] != nums[second-1]):
                            break
                elif total > 0:
                    second += 1
                elif total < 0:
                    third -= 1
        res = set(tuple(l) for l in res)
        res = [list(t) for t in res]
        return res

    def threeSum2(self, nums):
        if len(nums) < 3:
            return []        
        nums.sort()
        print(nums)
        answer_list = []
        for first_position in range(0, len(nums)-2, 1):
            second_position = first_position + 1
            third_position = len(nums) - 1
            while (second_position != third_position):
                total = (nums[first_position] + nums[second_position])
                total = total + nums[third_position]
                if total == 0:
                    answer_list.append([nums[first_position], nums[second_position], nums[third_position]])
                    while(second_position < third_position):
                        second_position += 1
                        if(nums[second_position] != nums[second_position-1]):
                            break
                    while(third_position > second_position):
                        third_position -= 1
                        if(nums[third_position] != nums[third_position+1]):
                            break
                elif total < 0:
                    second_position += 1
                elif total > 0:
                    third_position -=1
        answer_list = set(tuple(l) for l in answer_list)
        answer_list = [list(t) for t in answer_list]
        return answer_list


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    res = s.threeSum(nums)
    print('res', res)

