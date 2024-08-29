class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        f = [[] for i in range(len(nums) + 1)]
        
        for i in range(len(nums)):
            if freq.get(nums[i]):
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        
        for n, c in freq.items():
            f[c].append(n)

        res = []
        for i in range(len(f) - 1, 0, -1):
            for n in f[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        