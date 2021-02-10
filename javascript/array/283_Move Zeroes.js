/*
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]

Reference
    - https://leetcode.com/problems/move-zeroes/
*/

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */

// ! This solution is not for modifing nums in-place instead.
//  var moveZeroes = (nums) => {
//     // using space to deal with it.
//     let res = [],
//         num_of_zero = 0;

//     for (let i=0, max=nums.length; i<max; i++) {
//         if (nums[i] === 0) {
//             num_of_zero += 1;
//         } else {
//             res.push(nums[i]);
//         }
//     }

//     for (let j=0, max_=num_of_zero; j<max_; j++) {
//         res.push(0);
//     }
//     return res;
//  }

var moveZeroes = (nums) => {
    let num_of_zero = 0,
        modified_num_index = 0;

    for (let i=0, max=nums.length; i<max; i++) {
        if (nums[i] === 0) {
            num_of_zero += 1;
        } else {
            nums[modified_num_index] = nums[i];
            modified_num_index += 1;
        }
    }

    for (let j=nums.length - num_of_zero, max=nums.length; j<max; j++) {
        nums[j] = 0;
    }
}


var nums = [0, 1, 0, 3, 12];
var res = moveZeroes(nums);

