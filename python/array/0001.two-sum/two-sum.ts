



{
  /**
   * 時間複雜度最佳解法 O(n)
   * @param nums 
   * @param target 
   * @returns 
   */
  function twoSumBestTimeComplexity(nums: number[], target: number): number[] {

    const hashTable: {[key: number]: number} = {};

    for (let i=0; i<nums.length; i++) {
      const diff = target - nums[i];
      
      if (hashTable.hasOwnProperty(diff)) {
        return [hashTable[diff], i]
      }
      hashTable[nums[i]] = i;
    }
    throw new Error('no two sum solution.');
  }


  const res = twoSumBestTimeComplexity([2,7,11,15], 9);
  console.log(res);
}


// {
//   function twoSumBestSpaceComplexity() {

//   }


// }


// {
//   function twoSumBalance() {

//   }


// }