function majorityElement(nums: number[]): number {
    if (nums.length === 1) return nums[0];
    let map = {};

    for (let i = 0; i < nums.length; i++) {
        if (map[nums[i]]) {
            map[nums[i]]++;
            if (map[nums[i]] > nums.length / 2) {
                return nums[i];
            }
        } 
        else map[nums[i]] = 1;
    }
};