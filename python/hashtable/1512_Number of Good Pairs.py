"""
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

 
Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:
Input: nums = [1,2,3]
Output: 0
 

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100

# Reference 
    - https://leetcode.com/problems/number-of-good-pairs/
    - https://www.youtube.com/watch?v=ryykpSW-g4M

"""
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]):
        # Runtime: 32 ms, faster than 77.55%, Memory Usage: 14.3 MB, less than 11.53%
        """ 較佳解法 """
        d, count = {}, 0
        
        for i in nums:
            count += d.setdefault(i, 0)
            d[i] += 1
        return count


if __name__ == '__main__':
    nums = [1,2,3,1,1,3]

    s = Solution()
    res = s.numIdenticalPairs(nums)
    print('res', res)


    # setdefault 用法
    d = {'Name': 'Zara', 'Age': 7}
    d.setdefault('Age', None) # 7 
    d.setdefault('Sex', None) # None.

    

