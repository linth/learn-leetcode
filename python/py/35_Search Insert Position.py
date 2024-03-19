'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

'''
from typing import List


class Solution:
    # def bisect(self, nums, target):
    #     # Solution 1: bisect
    #     # https://leetcode.com/problems/search-insert-position/discuss/679918/Python-2-Solutions%3A-Oneliner-and-Classical-BS-explained
    #     return bisect.bisect_left(nums, target)
    
    def searchInsert(self, nums: List[int], target: int):
        # Solution 2: Classical binary search
        beg, end = 0, len(nums)
        while beg < end:
            mid = (beg + end)//2
            if nums[mid] >= target:
                end = mid
            else:
                beg = mid + 1
        return beg
        
    

if __name__ == '__main__':
    s = Solution()
    
    nums = [1,3,5,6]
    res = s.searchInsert(nums, 5)
    print(res)
    
    nums = [1,3,5,6]
    res = s.searchInsert(nums, 7)
    print(res)