class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n,0) + 1
        freq = [[] for _ in range(len(nums) + 1)]
        print(count)
        for num, cnt in count.items():
            print(cnt, num)
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
