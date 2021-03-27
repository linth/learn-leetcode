"""
Given a rows x cols binary matrix filled with 0's and 1's, 
find the largest rectangle containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:
Input: matrix = []
Output: 0

Example 3:
Input: matrix = [["0"]]
Output: 0

Example 4:
Input: matrix = [["1"]]
Output: 1

Example 5:
Input: matrix = [["0","0"]]
Output: 0
 

Constraints:
- rows == matrix.length
- cols == matrix[i].length
- 0 <= row, cols <= 200
- matrix[i][j] is '0' or '1'.

Reference
    - https://leetcode.com/problems/maximal-rectangle/
"""
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]):
        if not matrix: 
            return 0

        if not matrix:
            return 0
        res = 0
        height = [0] * len(matrix[0])
        for row in matrix:
            for i in range(len(matrix[0])):
                if row[i] == '0':
                    height[i] = 0
                else:
                    height[i] += 1
            res = max(res, self.maxRect(height))
        return res

    def maxRect(self, height):
        res = 0
        stack = []
        height.append(0)
        for i in range(len(height)):
            if not stack or height[i] > height[stack[-1]]:
                stack.append(i)
            else:
                while stack and height[stack[-1]] > height[i]:
                    w = height[stack[-1]]
                    stack.pop()
                    h = i if not stack else i - stack[-1] - 1
                    res = max(res, w * h)
                stack.append(i)
        return res


if __name__ == '__main__':
    
    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"],
    ]

    matrix2 = []

    s = Solution()
    res = s.maximalRectangle(matrix2)
    print('res', res)
