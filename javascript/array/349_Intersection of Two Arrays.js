/*
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
Output: [2]

Example 2:
Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
Output: [9, 4]

=====
Note:
=====
Each element in the result must be unique.
The result can be in any order.

Reference:
    - https://leetcode.com/problems/intersection-of-two-arrays/
*/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */

var intersection = (nums1, nums2) => {
    let res = [];

    // delete the duplicated number.
    // nums1.sort();
    // nums2.sort();

    // console.log('nums1', nums1); // 排序不一定是穩定的.    
    // console.log('nums2', nums2);

    for (let i=0, max=nums1.length; i<max; i++) {
        for (let j=0, max_=nums2.length; j<max_; j++) {
            if (nums1[i] === nums2[j]) {
                if (res.indexOf(nums1[i]) === -1) {
                    res.push(nums1[i]);
                }
            }
        }
    }
    return res;
};


var nums1 = [1, 2, 2, 1];
var nums2 = [2, 2];
var res = intersection(nums1, nums2);
console.log('res', res);


