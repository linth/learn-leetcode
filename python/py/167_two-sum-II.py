"""
No. 167. Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

reference:
    - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
from typing import List


class Solution:
    def first_time(self, numbers, target):
        """
        solve this issue at first time.
        :param numbers:
        :param target:
        :return:
        """
        d = {}
        for i in range(len(numbers)):
            n = target - numbers[i]
            if n in numbers:
                if numbers.index(n) > i:
                    return [i+1, numbers.index(n)+1]
                elif numbers.index(n) == i:
                    return [i+1, numbers.index(n)+2]
            else:
                pass

    def online1(self, numbers, target):
        d = {}
        for i in range(len(numbers)):
            if numbers[i] not in d:
                d[target-numbers[i]] = i
            else:
                return [d[numbers[i]]+1, i+1]

    def two_sum(self, number, target):
        pass


def main():
    # numbers = [2, 7, 11, 15]
    numbers = [0, 0, 3, 4]
    # target = 9
    target = 0
    s = Solution()
    # res = s.first_time(numbers, target)
    res = s.online1(numbers, target)
    print('The res = {}'.format(res))


if __name__ == '__main__':
    main()
