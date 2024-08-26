function findNumbers(nums: number[]): number {
    let even = 0;
    
    for (let i = 0; i < nums.length; i++) {
        let j = 1;
        while (nums[i] >= 10) {
            nums[i] = nums[i] / 10;
            j++;
        }
        if (j % 2 === 0) even++;
    }
    
    return even;
};