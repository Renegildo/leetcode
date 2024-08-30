class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        longest = 1
        largest = float("-inf")
        numbers = {}
        
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] > largest:
                largest = nums[i]
            numbers[nums[i]] = True 
        
        current = 1
        
        for k in numbers:
            if numbers.get(k + 1):
                current += 1
                if current > longest:
                    longest = current
            else:
                current = 1

        return longest
