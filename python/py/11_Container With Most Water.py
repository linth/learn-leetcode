"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.


Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Constraints:
n == height.length
2 <= n <= 3 * 104
0 <= height[i] <= 3 * 104

Reference:
    - https://leetcode.com/problems/container-with-most-water/
    - https://leetcode.com/problems/container-with-most-water/discuss/1069698/Python-O(n)-by-two-pointers-w-Comment
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """ origin method. """
        h = len(height)
        max_area = 0

        for i in range(h):
            # print('i->', i, '=>', height[i])
            for j in range(i+1, h):
                # print('  j->', j, height[j])
                if max_area <= abs(i-j) * min(height[i], height[j]):
                    max_area = abs(i-j) * min(height[i], height[j])
        return max_area

    def max_area(self, height: List[int]) -> int:
        """ while-loop method. """
        h = len(height)
        max_area = 0
        left, right = 0, h-1

        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
    res = s.max_area(height)
    print('res', res)

