class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        lst = [[] for _ in range(len(nums) + 1)]
        for key,v in freq.items():
            lst[v].append(key)
        
        for l in lst[::-1]:
            for n in l:
                res.append(n)
                
                if len(res)==k:
                    print(len(res), res)
                    return res
                