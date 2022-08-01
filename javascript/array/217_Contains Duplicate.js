/**
 * Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
 * 
Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109


Reference:
    - https://leetcode.com/problems/contains-duplicate/submissions/

 */


/**
 * @param {number[]} nums
 * @return {boolean}
 */
 var containsDuplicate = function(nums) {
    
    let s = new Set(nums);   
    
    if (s.size != nums.length) {
        return true;
    }
    
    return false;
};