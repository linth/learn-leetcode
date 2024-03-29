from typing import List


class Solution(object):
    def twoSum0(self, nums, target):
        """
        nums = [2, 7, 11, 15], target = 9

        :param nums:
        :param target:
        :return:
        """
        pass

    def brute_force(self, nums, target):
        """
        brute force.

        :param nums:
        :param target:
        :return:
        """
        n = len(nums)

        for i, v in enumerate(nums):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
    
    def use_sorting(self, nums, target):
        """ 這樣的方法似乎不適用，因為sorting完後會破壞整個list. """
        # sort the list.
        nums.sort()

        # maintain two indices
        (low, high) = (0, len(nums)-1)

        while low < high:
            if nums[low] + nums[high] == target:
                return (low, high)

            if nums[low] + nums[high] < target:
                low = low + 1
            else:
                high = high - 1


    def hashmap_method(self, nums, target):
        """
        較佳解法

        :param nums:
        :param target:
        :return:
        """
        d = {}

        for k, v in enumerate(nums):
            diff = target - v

            # 使用dict來記錄value的index值。
            if diff not in d:
                d[v] = k # {value: index}
            else:
                return [d[diff], k]

    def twoSum3(self, nums, target):
        """
        :param nums:
        :param target:
        :return:
        """
        # two points.
        begin, end = 0, len(nums) - 1

        nums_index = [(v, index) for index, v in enumerate(nums)]
        nums_index.sort()
        # print('nums_index', nums_index)

        while begin < end:
            curr = nums_index[begin][0] + nums_index[end][0]

            if curr == target:
                return [nums_index[begin][1], nums_index[end][1]]
            elif curr < target:
                begin += 1
            else:
                end -= 1

    def twoSum4(self, nums, target):
        """ two-pass hash table. """
        pass

    def twoSum5(self, nums, taget):
        """ one-pass hash table. """
        pass

    # def maxValueTwoSum(self, nums):
    #     """ get max value for two numbers in an array. """
    #     max_val = 0

    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if max_val <= nums[i] + nums[j]:
    #                 max_val = nums[i] + nums[j]
    #     return max_val


if __name__ == '__main__':
    nums = [2, 11, 7, 15]
    target = 9

    s = Solution()
    # res = s.twoSum(nums, target)
    res = s.hashmap_method(nums, target)
    # res = s.twoSum3(nums, target)
    # res = s.maxValueTwoSum(nums)
    print('res', res)
