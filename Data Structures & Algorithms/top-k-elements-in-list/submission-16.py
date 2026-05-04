class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        res = []
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for key,val in count.items():
            freq[val].append(key)
        for f in freq[::-1]:
            for n in f:
                res.append(n)
                if len(res)==k:
                    return res