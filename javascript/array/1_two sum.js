/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Reference:
    - https://leetcode.com/problems/two-sum/
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */


var twoSum = function(nums, target) {

    // 請注意看 for-loop condition.
    for (let i=0, max=nums.length; i<max; i++) {
        for (let j=i+1, max_=nums.length; j<max_; j++) {
            if (nums[j] + nums[i] === target) {
                return [i, j];
            }
        }
    }

    // TODO: please find out another better way to solve the problem.
};


var nums = [3, 2, 4];
var target = 6;
var result = twoSum(nums, target);
console.log('result: ', result);


