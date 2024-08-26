function sortedSquares(nums: number[]): number[] {
    for (let i = 0; i < nums.length; i++) {
        nums[i] = nums[i] * nums[i]
    }
  
    
    for (let j = 0; j < nums.length; j++) {
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] < nums[i - 1]) {
            let tmp = nums[i];
            nums[i] = nums[i - 1];
            nums[i - 1] = tmp;
        }
    }
      
    }
    
    return nums;
};