class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}

        for i in range(len(nums)):
            if freq.get(nums[i]) == 1:
                return True
            else:
                freq[nums[i]] = 1
        
        return False
        