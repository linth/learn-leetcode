"""
References
- https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
"""
from typing import List


# class Solution:
#     def sumOddLengthSubarrays(self, arr: List[int]) -> int:
#         # 2 * n + 1, (1, 3, 5, ..., etc.)
#         max_length = len(arr)
#
#         odd_arr = []
#         # general an array. [1, 3, 5, ...]
#         for i in range(0, max_length):
#             v = 2 * i + 1
#             if v <= max_length:
#                 odd_arr.append(v)
#         # print(odd_arr)
#
#         for o in odd_arr:
#             # print(o) # 1, 3, 5, ...
#             for i, v in enumerate(arr):
#                 gen_arr = []
#                 if i + o <= max_length:
#                     for j in range(1, o):
#                         # print('j: ', j)
#                         gen_arr.append(v)
#                         print(f'length: {o}, index: {i}, values: {v}, arr: {gen_arr}, j: {j}')
#
#
# if __name__ == '__main__':
#     arr = [1, 4, 2, 5, 3]
#     s = Solution()
#     s.sumOddLengthSubarrays(arr)
