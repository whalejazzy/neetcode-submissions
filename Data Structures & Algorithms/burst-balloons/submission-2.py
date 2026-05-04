class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache = {}
        
        nums.insert(0,1)
        nums.append(1)

        def dfs(l, r):
            if (l, r) in cache:
                return cache[(l, r)]
            if l > r or r < l:
                return 0
        
            
            res = 0
            print(l, r)
            for i in range(l, r + 1):
                res = max(res, dfs(i + 1, r) + dfs(l, i - 1) + nums[l- 1] * nums[i] * nums[r + 1])
            cache[(l, r)] = res
            return res
        
        return dfs(1, len(nums) - 2)

                

            