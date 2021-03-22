/*
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

Reference:
    - https://leetcode.com/problems/longest-substring-without-repeating-characters/
*/

/**
 * @param {string} s
 * @return {number}
 */

var lengthOfLongestSubstring = (s) => {
    let n = s.length;
    let ans = 0;

    for (let i=0; i<n; i++) {
        let j = i; 

        while (j<n) {
            ans = Math.max(ans, j - i);
        }
    }
    console.log('ans', ans);
    return ans;
};


 var s = "abcabcbb";
//var s = 'pwwkew';
//var res = lengthOfLongestSubstring(s);
//console.log('res', res);

for (let i=0, max=s.length; i<max; i++) {
    console.log('->', s[i]);
}
